SELECT
   doi,
   crossref,
   (SELECT as STRUCT * from `{mag}` as mag WHERE mag.Doi = UPPER(TRIM(doi))) as mag,
   (SELECT as STRUCT * from `{openalex}` as openalex WHERE openalex.Doi = UPPER(TRIM(doi))) as openalex,
FROM `{doi_table}`