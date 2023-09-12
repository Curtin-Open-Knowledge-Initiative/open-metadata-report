--- collating information from OpenAIRE tables
--- currently, sharded table hard-coded should replace by injecting data from parameters
--- note: currently, an (explicitly declared) subset of relations table is used that contains only relations between results and organizations+projects
--- #TODO create paths to source tables i.s.o. explicitly declaring them
--- #TODO replace subset of relations table with the real deal

--- Affiliatons
--- generate column with unique RORs per id from organizations table
--- note: a handful of RORs (n=26) is in the table without url-prefix or other errors - leave as is for now
WITH RORS_ARRAY AS (
  SELECT
    id,
    ARRAY_AGG(rors) as ror
  FROM (
    SELECT DISTINCT id, pid_check.value as rors,
    FROM `academic-observatory.openaire.organization20230817`,
    UNNEST (pid) as pid_check
    WHERE pid_check.scheme = 'ROR')
  GROUP BY id
),
--- collect other information from organizations table and join with RORs
AFFILIATIONS AS (
SELECT
o.id,
STRUCT(o.id, o.legalname, o.country.code as country, o.pid, r.ror) as organization
FROM `academic-observatory.openaire.organization20230817` as o
LEFT JOIN RORS_ARRAY as r ON o.id = r.id
),

--- Projects
--- only collecting funder names at the moment - these are harmonized and can be used as ids
--- note: project id also encodes funders - could be useful as well
PROJECTS AS (
  SELECT
    id,
    STRUCT(id, ARRAY_AGG(funder) as funder) as project,
  FROM (
    SELECT DISTINCT id, funding.shortname as funder
    FROM `academic-observatory.openaire.project20230817`,
    UNNEST(funding) as funding)
  GROUP BY id
),

--- Collect information from each table (publication, dataset, software, otherresearchproduct)
SOURCES AS (

   SELECT

   publications.id,
   pid,
   type, --- publication, dataset, software or other
   publicationdate,
   ARRAY(SELECT AS STRUCT fullname, rank, pid.id FROM unnest(author)) as author,
   STRUCT(
      container.name as name,
      container.issnOnline as issnOnline,
       container.issnPrinted as issnPrinted,
       container.issnLinking as issnLinking
   ) as container,
   publisher,
   CASE
      WHEN ARRAY_LENGTH(description) > 0 THEN ARRAY_TO_STRING(description, '')
      ELSE NULL
   END
   as description,
   ARRAY(SELECT AS STRUCT subject.value, subject.scheme FROM unnest(subjects)) as subject,
   ARRAY(SELECT AS STRUCT GENERATE_UUID() as uuid, publicationdate, type, pid FROM unnest(instance)) as instance,

   FROM `academic-observatory.openaire.publication20230817` as publications

UNION ALL

   SELECT

   publications.id,
   pid,
   type, --- publication, dataset, software or other
   publicationdate,
   ARRAY(SELECT AS STRUCT fullname, rank, pid.id FROM unnest(author)) as author,
   null as container, --- tables dataset, software, otherresearchproduct have no variable container
   publisher,
   CASE
      WHEN ARRAY_LENGTH(description) > 0 THEN ARRAY_TO_STRING(description, '')
      ELSE NULL
   END
   as description,
   ARRAY(SELECT AS STRUCT subject.value, subject.scheme FROM unnest(subjects)) as subject,
   ARRAY(SELECT AS STRUCT GENERATE_UUID() as uuid, publicationdate, type, pid FROM unnest(instance)) as instance,

   FROM `academic-observatory.openaire.dataset20230817` as publications

UNION ALL

   SELECT

   publications.id,
   pid,
   type, --- publication, dataset, software or other
   publicationdate,
   ARRAY(SELECT AS STRUCT fullname, rank, pid.id FROM unnest(author)) as author,
   null as container, --- tables dataset, software, otherresearchproduct have no variable container
   publisher,
   CASE
      WHEN ARRAY_LENGTH(description) > 0 THEN ARRAY_TO_STRING(description, '')
      ELSE NULL
   END
   as description,
   ARRAY(SELECT AS STRUCT subject.value, subject.scheme FROM unnest(subjects)) as subject,
   ARRAY(SELECT AS STRUCT GENERATE_UUID() as uuid, publicationdate, type, pid FROM unnest(instance)) as instance,

   FROM `academic-observatory.openaire.software20230817` as publications


UNION ALL

   SELECT

   publications.id,
   pid,
   type, --- publication, dataset, software or other
   publicationdate,
   ARRAY(SELECT AS STRUCT fullname, rank, pid.id FROM unnest(author)) as author,
   null as container, --- tables dataset, software, otherresearchproduct have no variable container
   publisher,
   CASE
      WHEN ARRAY_LENGTH(description) > 0 THEN ARRAY_TO_STRING(description, '')
      ELSE NULL
   END
   as description,
   ARRAY(SELECT AS STRUCT subject.value, subject.scheme FROM unnest(subjects)) as subject,
   ARRAY(SELECT AS STRUCT GENERATE_UUID() as uuid, publicationdate, type, pid FROM unnest(instance)) as instance,

   FROM `academic-observatory.openaire.otherresearchproduct20230817` as publications
),

--- add affiliations and projects
TABLE_FROM_SOURCE AS (

SELECT

publications.*,
affiliations.organization as organization,
projects.project as project

FROM SOURCES as publications

---- add affiliations and projects
--- use temporary relations table for now
--- note: all relations between result and organization have reltype.type 'affiliation'
LEFT JOIN (SELECT
  publications.id as id,
  ARRAY_AGG(organizations.organization IGNORE NULLS) as organization
  FROM SOURCES as publications
  LEFT JOIN (SELECT * FROM `academic-observatory.openaire.relation20230817` WHERE targetType = 'organization') as relations
  ON publications.id = relations.source
  LEFT JOIN AFFILIATIONS as organizations
  ON relations.target = organizations.id
  GROUP BY publications.id) as affiliations
ON publications.id = affiliations.id

--- add projects
--- use temporary relations table for now
--- note: all relations between results and project have relype.type 'outcome'
LEFT JOIN (SELECT
  publications.id as id,
  ARRAY_AGG(p.project IGNORE NULLS) as project
  FROM SOURCES as publications
  LEFT JOIN (SELECT * FROM `academic-observatory.openaire.relation20230817` WHERE targetType = 'project') as relations
  ON publications.id = relations.source
  LEFT JOIN PROJECTS as p
  ON relations.target = p.id
  GROUP BY publications.id) as projects
ON publications.id = projects.id

),

--- extract dois from nested column pids
--- note: tables other than publication have pid.value and pid.scheme inversed...
DOIS AS (

 SELECT
  id,
  CASE
    WHEN pid_check.scheme = 'doi' THEN pid_check.value
    WHEN pid_check.value = 'doi' THEN pid_check.scheme
    ELSE null
  END as doi
 FROM TABLE_FROM_SOURCE,
 UNNEST (pid) as pid_check
 --- WHERE clause below is probably superfluous now
 WHERE pid_check.scheme = 'doi' OR pid_check.value = 'doi'
 ),

INTERMEDIATE AS (

 SELECT

 publications.id,
 dois.doi,
 publications.* EXCEPT (id)

 FROM TABLE_FROM_SOURCE as publications
 LEFT JOIN DOIS as dois
 ON publications.id = dois.id
 )

--- TRUTHTABLE

--- Notes:
--- currently rank arbitrarily by hashing OpenAIRE id - consider choice of hash method?
--- author.fullname has no empty strings
--- description can contain, but is not limited to abstracts - proceed to use with caution
--- currently, only ids are orcid/orcid_pending, and id field is not nested. This may change in future (still true for 20230817)
--- no empty fields for affiliations, so ARRAY_LENGTH taken as not all affiliations have string field
--- container is not nested
--- container.name has no empty strings
--- issn fields do have empty strings
--- issnOnline and issnPrinting have varying string length, but 99.8/99.9% of non-empty strings have length 8-9, so 1 ISSN
--- issnLinking contains only empty strings (and NULLs)
--- funder names (also short names as used here) are harmonized so can be used as source ids

SELECT

  UPPER(TRIM(doi)) as doi,
  id as source_id,
  type,
  EXTRACT(YEAR FROM publicationdate) as published_year,
  RANK() OVER (ORDER BY FARM_FINGERPRINT(id)) as deduplication_rank,


--- Authors
  CASE
    WHEN (SELECT COUNT(1) FROM UNNEST(author) AS authors WHERE authors.fullname is not null) > 0 THEN TRUE
    ELSE FALSE
  END as has_authors,
  ARRAY_LENGTH(author) as count_authors,
  CASE
    WHEN (SELECT COUNT(1) FROM UNNEST(author) AS authors WHERE authors.fullname is not null) > 0 THEN TRUE
    ELSE FALSE
  END as has_authors_string,
  (SELECT COUNT(1) FROM UNNEST(author) AS authors WHERE authors.fullname is not null) as count_authors_string,
  CASE
    WHEN (SELECT COUNT(1) FROM UNNEST(author) AS authors WHERE authors.id.scheme LIKE '%orcid%') > 0 THEN TRUE
    ELSE FALSE
  END as has_authors_id_orcid,
  (SELECT COUNT(1) FROM UNNEST(author) AS authors WHERE authors.id.scheme  LIKE '%orcid%') as count_authors_id_orcid,
  CASE
    WHEN (SELECT COUNT(1) FROM UNNEST(author) AS authors WHERE authors.rank is not null) > 0 THEN TRUE
    ELSE FALSE
  END as has_authors_sequence,
  (SELECT COUNT(1) FROM UNNEST(author) AS authors WHERE authors.rank is not null) as count_authors_sequence,

  --- Affiliations
   CASE
    WHEN ARRAY_LENGTH(organization) > 0 THEN TRUE
    ELSE FALSE
  END as has_affiliations,
  ARRAY_LENGTH(organization) as count_affiliations,
  CASE
    WHEN (SELECT COUNT(1) FROM UNNEST(organization) AS affiliations WHERE affiliations.legalname is not null) > 0 THEN TRUE
    ELSE FALSE
  END as has_affiliations_string,
  (SELECT COUNT(1) FROM UNNEST(organization) AS affiliations WHERE affiliations.legalname is not null) as count_affiliations_string,
  CASE
    WHEN (SELECT COUNT(1) FROM UNNEST(organization) AS affiliations WHERE affiliations.id is not null) > 0 THEN TRUE
    ELSE FALSE
  END as has_affiliations_id_source,
  (SELECT COUNT(1) FROM UNNEST(organization) AS affiliations WHERE affiliations.id is not null) as count_affiliations_id_source,
  CASE
    WHEN (SELECT COUNT(1) FROM UNNEST(organization) AS affiliations WHERE affiliations.ror is not null) > 0 THEN TRUE
    ELSE FALSE
  END as has_affiliations_id_ror,
  (SELECT COUNT(1) FROM UNNEST(organization) AS affiliations WHERE affiliations.ror is not null) as count_affiliations_id_ror,
  CASE
    WHEN (SELECT COUNT(1) FROM UNNEST(organization) AS affiliations WHERE affiliations.country is not null) > 0 THEN TRUE
    ELSE FALSE
  END as has_affiliations_id_countrycode,
  (SELECT COUNT(1) FROM UNNEST(organization) AS affiliations WHERE affiliations.country is not null) as count_affiliations_id_countrycode,
  --- Abstract
  CASE
    WHEN (description is not null) THEN TRUE
    ELSE FALSE
  END as has_abstract,
  LENGTH(description) as count_abstract,
  ---
  --- Citations
  false as has_citations, --- revisit how missing columns are handled
  --- References
  false as has_references, --- revisit how missing columns are handled
  ---
  --- Fields
  CASE
    WHEN ARRAY_LENGTH(subject) > 0 THEN TRUE
    ELSE FALSE
  END as has_fields,
  CASE
    WHEN ARRAY_LENGTH(subject) > 0 THEN ARRAY_LENGTH(subject)
    ELSE null
  END as count_fields,
--- top_field
--- Venue
--- for non-publication type, use publisher as proxy for venue (string only)
  CASE
    WHEN type != 'publication' AND publisher is not null THEN TRUE
    WHEN container.name is not null
    THEN TRUE
    ELSE FALSE
  END as has_venue,
  CASE
    WHEN type != 'publication' AND publisher is not null THEN 1
    WHEN container.name is not null
    THEN 1
    ELSE 0
    END as count_venue,
  CASE
    WHEN type != 'publication' AND publisher is not null THEN TRUE
    WHEN container.name is not null
    THEN TRUE
    ELSE FALSE
  END as has_venue_string,
  CASE
    WHEN type != 'publication' AND publisher is not null THEN 1
    WHEN container.name is not null
    THEN 1
    ELSE 0
  END as count_venue_string,
  CASE
    WHEN (CHAR_LENGTH(container.issnOnline)  > 0 OR CHAR_LENGTH(container.issnPrinted) > 0)
    THEN TRUE
    ELSE FALSE
  END as has_venue_id_issn,
  CASE
    WHEN (CHAR_LENGTH(container.issnOnline)  > 0) IS FALSE AND (CHAR_LENGTH(container.issnPrinted) > 0) IS FALSE THEN 0
    WHEN (CHAR_LENGTH(container.issnOnline)  > 0) IS TRUE AND (CHAR_LENGTH(container.issnPrinted) > 0) IS FALSE THEN 1
    WHEN (CHAR_LENGTH(container.issnOnline)  > 0) IS FALSE AND (CHAR_LENGTH(container.issnPrinted) > 0) IS TRUE THEN 1
    WHEN (CHAR_LENGTH(container.issnOnline)  > 0) IS TRUE AND (CHAR_LENGTH(container.issnPrinted) > 0) IS TRUE THEN 2
    ELSE 0
  END as count_venue_id_issn,
  CASE
    WHEN CHAR_LENGTH(container.issnLinking) > 0 THEN TRUE
    ELSE FALSE
  END as has_venue_id_issnl,
  CASE
    WHEN CHAR_LENGTH(container.issnLinking) > 0 THEN 1
    ELSE 0
  END as count_venue_id_issnl,

--- Funders
  CASE
    WHEN ARRAY_LENGTH(project) > 0 THEN TRUE
    ELSE FALSE
  END as has_funders,
  ARRAY_LENGTH(project) as count_funders,
  CASE
    WHEN (SELECT COUNT(1) FROM UNNEST(project) AS funders WHERE  funders.funder is not null) > 0 THEN TRUE
    ELSE FALSE
  END as has_funders_string,
  (SELECT COUNT(1) FROM UNNEST(project) AS  funders WHERE  funders.funder is not null) as count_funders_string,
  CASE
    WHEN (SELECT COUNT(1) FROM UNNEST(project) AS  funders WHERE  funders.funder is not null) > 0 THEN TRUE
    ELSE FALSE
  END as has_funders_id_source,
  (SELECT COUNT(1) FROM UNNEST(project) AS  funders WHERE funders.funder is not null) as count_funders_id_source

FROM INTERMEDIATE
---FROM `utrecht-university.TEMP.openaire_publications_intermediate`
