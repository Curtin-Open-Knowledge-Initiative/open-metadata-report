SELECT
    published_year,
    type,
    field,
    COUNT(DISTINCT doi) as num_dois,
    COUNT(DISTINCT IF(has_affiliation_id, doi, null)) as dois_with_affiliation_ids,
    COUNT(DISTINCT IF(has_gridid, doi, null) as dois_with_grids,
    COUNT(DISTINCT IF(has_affiliation_string, doi, null) as dois_with_affiliation_strings,
    COUNT(DISTINCT IF(has_abstract, doi, null)) as dois_with_abstract,
    COUNT(DISTINCT IF(has_citation, doi, null)) as dois_with_citations,
    COUNT(DISTINCT IF(has_references, doi, null)) as dois_with_references,
    COUNT(DISTINCT IF(num_fields > 1, doi, null)) as dois_with_more_than_one_field,

    COUNT(DISTINCT source_id) as num_objects,
    COUNT(DISTINCT IF(has_affiliation_id, source_id, null)) as objects_with_affiliation_ids,
    COUNT(DISTINCT IF(has_gridid, source_id, null)) as objects_with_grids,
    COUNT(DISTINCT IF(has_affiliation_string, source_id, null)) as objects_with_affiliation_strings,
    COUNT(DISTINCT IF(has_abstract, source_id, null)) as objects_with_abstract,
    COUNT(DISTINCT IF(has_citations, source_id, null)) as objects_with_citations,
    COUNT(DISTINCT IF(has_references, source_id, null)) as objects_with_references,
    COUNT(DISTINCT IF(num_fields > 1, source_id, null)) as objects_with_more_than_one_field,

    COUNT(DISTINCT IF(doi_not_canonical_family, doi, null)) as doi_not_canonical_family

FROM {table}
GROUP BY published_year, type, field
ORDER BY published_year DESC, type ASC, field ASC
