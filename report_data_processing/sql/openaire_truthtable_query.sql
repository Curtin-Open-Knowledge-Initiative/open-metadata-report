--- adding information from OpenAIRE tables

---Affiliatons
--- generate column with unique RORs from organizations table
--- Note: a handful of RORs (n=26) is in the table without url-prefix or other errors
WITH RORS_EXTRACTED AS (
SELECT DISTINCT
  id,
  pid_check.value as rors,

 FROM `academic-observatory.openaire.organization`,
 UNNEST (pid) as pid_check
 WHERE pid_check.scheme = 'ROR'
),
--- aggregate into array
RORS_ARRAY AS (
  SELECT
    id,
    ARRAY_AGG(rors) as ror
  FROM RORS_EXTRACTED
  GROUP BY id
),
--- collect other information from organizations table and join with RORs
AFFILIATIONS AS (
SELECT
o.id,
o.legalname,
o.country.code as country,
o.pid,
r.ror
FROM `academic-observatory.openaire.organization` as o
LEFT JOIN RORS_ARRAY as r ON o.id = r.id
),

TABLE_FROM_SOURCE AS (

SELECT

id,
pid,
publicationdate,
ARRAY(SELECT AS STRUCT fullname, rank, pid.id FROM unnest(author)) as author,
STRUCT(
        container.name as name,
        container.issnOnline as issnOnline,
        container.issnPrinted as issnPrinted,
        container.issnLinking as issnLinking
    ) as container,
 CASE
    WHEN ARRAY_LENGTH(description) > 0 THEN ARRAY_TO_STRING(description, '')
    ELSE NULL
 END
 as description,
ARRAY(SELECT AS STRUCT subject.value, subject.scheme FROM unnest(subjects)) as subject,
ARRAY(SELECT AS STRUCT GENERATE_UUID() as uuid, publicationdate, type, pid FROM unnest(instance)) as instance

FROM `utrecht-university.TEMP.openaire_publication`
),

---- extract dois from nested column pids
DOIS AS (

 SELECT
  id,
  pid_check.value as doi,
 FROM TABLE_FROM_SOURCE,
 UNNEST (pid) as pid_check
 WHERE pid_check.scheme = 'doi'
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

--- add Affilations
--- all relations between result and organization have reltype.type 'affiliation'
SELECT

a.id,
b.target.id as organization_id

FROM `utrecht-university.TEMP.openaire_publications_intermediate` as a
LEFT JOIN `academic-observatory.openaire.relation` as b
ON a.id = b.source.id

--- joining in 2 steps
WITH TABLE AS (

  SELECT

a.id,
STRUCT(b.id, b.legalname, b.country,	b.pid, b.ror) as organization

 FROM `utrecht-university.TEMP.openaire_relations_results_organizations_sample` as a
 LEFT JOIN `utrecht-university.TEMP.openaire_organizations`as b
 ON a.organization_id = b.id
)

SELECT

id,
ARRAY_AGG(organization) as organization

FROM TABLE
GROUP BY id


--- TRUTHTABLE

--- Notes:
--- author.fullname has no empty strings
--- description can contain, but is not limited to abstracts - proceed to use with caution
--- currently, only ids are orcid/orcid_pending, and id field is not nested. This may change in future
--- container is not nested
--- container.name has no empty strings
--- issn fields do have empty strings
--- issnOnline and issnPrinting have varying string length, but 99.8/99.9% of non-empty strings have length 8-9, so 1 ISSN
--- issnLinking contains only empty strings (and NULLs)

SELECT

  UPPER(TRIM(doi)) as doi,
  id as source_id,
  null as type, --- revisit for use in self-comparison (dois vs non-dois)
  EXTRACT(YEAR FROM publicationdate) as published_year,
  ---RANK() OVER (ORDER BY some_variable DESC) as deduplication_rank,

  --- extra columns to indicate presence of PID types
  CASE
    WHEN (SELECT COUNT(1) FROM UNNEST(pid) AS pids WHERE pids.scheme = 'doi') > 0 THEN TRUE
    ELSE FALSE
  END
  as has_pid_doi,
  CASE
    WHEN (SELECT COUNT(1) FROM UNNEST(pid) AS pids WHERE pids.scheme = 'hanlde') > 0 THEN TRUE
    ELSE FALSE
  END
  as has_pid_handle,
  CASE
    WHEN (SELECT COUNT(1) FROM UNNEST(pid) AS pids WHERE pids.scheme = 'pmid') > 0 THEN TRUE
    ELSE FALSE
  END
  as has_pid_pmid,
  CASE
    WHEN (SELECT COUNT(1) FROM UNNEST(pid) AS pids WHERE pids.scheme = 'pmc') > 0 THEN TRUE
    ELSE FALSE
  END
  as has_pid_pmc,
    CASE
    WHEN (SELECT COUNT(1) FROM UNNEST(pid) AS pids WHERE pids.scheme = 'arXiv') > 0 THEN TRUE
    ELSE FALSE
  END
  as has_pid_arxiv,

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
  END as has_authors_orcid,
  (SELECT COUNT(1) FROM UNNEST(author) AS authors WHERE authors.id.scheme  LIKE '%orcid%') as count_authors_orcid,
  CASE
    WHEN (SELECT COUNT(1) FROM UNNEST(author) AS authors WHERE authors.rank is not null) > 0 THEN TRUE
    ELSE FALSE
  END as has_authors_sequence,
  (SELECT COUNT(1) FROM UNNEST(author) AS authors WHERE authors.rank is not null) as count_authors_sequence,
  ---
  --- Affiliations
  ---
  CASE
    WHEN (description is not null) THEN TRUE
    ELSE FALSE
  END as has_abstract,
  LENGTH(description) as count_abstract,
  ---
  --- Citations
  --- References
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
  CASE
    WHEN container.name is not null
    THEN TRUE
    ELSE FALSE
  END as has_venue,
  CASE
    WHEN container.name is not null
    THEN 1
    ELSE 0
    END as count_venue,
  CASE
    WHEN container.name is not null
    THEN TRUE
    ELSE FALSE
  END as has_venue_string,
  CASE
    WHEN container.name is not null
    THEN 1
    ELSE 0
  END as count_venue_string,
  CASE
    WHEN (CHAR_LENGTH(container.issnOnline)  > 0 OR CHAR_LENGTH(container.issnPrinted) > 0)
    THEN TRUE
    ELSE FALSE
  END as has_venue_issn,
  CASE
    WHEN (CHAR_LENGTH(container.issnOnline)  > 0) IS FALSE AND (CHAR_LENGTH(container.issnPrinted) > 0) IS FALSE THEN 0
    WHEN (CHAR_LENGTH(container.issnOnline)  > 0) IS TRUE AND (CHAR_LENGTH(container.issnPrinted) > 0) IS FALSE THEN 1
    WHEN (CHAR_LENGTH(container.issnOnline)  > 0) IS FALSE AND (CHAR_LENGTH(container.issnPrinted) > 0) IS TRUE THEN 1
    WHEN (CHAR_LENGTH(container.issnOnline)  > 0) IS TRUE AND (CHAR_LENGTH(container.issnPrinted) > 0) IS TRUE THEN 2
    ELSE 0
  END as count_venue_issn,
  CASE
    WHEN CHAR_LENGTH(container.issnLinking) > 0 THEN TRUE
    ELSE FALSE
  END as has_venue_issnl,
  CASE
    WHEN CHAR_LENGTH(container.issnLinking) > 0 THEN 1
    ELSE 0
  END as count_venue_issnl
-- Funder


 FROM `utrecht-university.TEMP.openaire_publications_intermediate`

---- prep for affilitations
SELECT

id,
legalname,
country.code as country,
pid,
---something for ror

 FROM `academic-observatory.openaire.organization`