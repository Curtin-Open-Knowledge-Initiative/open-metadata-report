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

SELECT * FROM INTERMEDIATE