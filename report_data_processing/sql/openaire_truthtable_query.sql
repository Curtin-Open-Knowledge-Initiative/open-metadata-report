--- adding information from OpenAIRE tables
WITH TABLE_FROM_SOURCE AS (

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

---- continue to regular T/F columns

 FROM `utrecht-university.TEMP.openaire_publications_intermediate`
