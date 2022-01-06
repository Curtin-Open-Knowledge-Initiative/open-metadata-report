SELECT
   c.doi,
   ARRAY_AGG(crossref) as crossref,
   ARRAY_AGG(mag ORDER BY mag.CitationCount DESC) as mag,
   ARRAY_AGG(openalex ORDER BY openalex.CitationCount DESC) as openalex
FROM `{doi_table}` as c
LEFT JOIN `{mag_intermediate}` as mag ON UPPER(TRIM(c.doi)) = UPPER(TRIM(mag.Doi))
LEFT JOIN `{openalex_intermediate}` as openalex ON UPPER(TRIM(openalex.Doi)) = UPPER(TRIM(c.doi))
GROUP BY doi