WITH TABLE AS (

SELECT

id,
pid,
author,
container,
ARRAY_LENGTH(description) as description_length,
 CASE
    WHEN ARRAY_LENGTH(description) > 0 THEN ARRAY_TO_STRING(description, '')
    ELSE NULL
 END
 as description,
subjects,
instance

FROM `utrecht-university.TEMP.openaire_publication`
)

SELECT * FROM TABLE