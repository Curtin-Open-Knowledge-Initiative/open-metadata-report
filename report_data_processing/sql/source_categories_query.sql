SELECT
    Year,
    DocType as type,
    field,
    COUNTIF(Doi is not null) as num_dois,
    COUNTIF(has_affiliation_id and Doi is not null) as dois_with_affiliation_ids,
    COUNTIF(has_gridid and Doi is not null) as dois_with_grids,
    COUNTIF(has_affiliation_string and Doi is not null) as dois_with_affiliation_strings,
    COUNTIF(has_abstract and Doi is not null) as dois_with_abstract,
    COUNTIF(has_citations and Doi is not null) as dois_with_citations,
    COUNTIF(has_references and Doi is not null) as dois_with_references,
    COUNTIF(num_fields > 1 and Doi is not null) as dois_with_more_than_one_field,

    COUNT(PaperId) as num_objects,
    COUNTIF(has_affiliation_id) as objects_with_affiliation_ids,
    COUNTIF(has_gridid) as objects_with_grids,
    COUNTIF(has_affiliation_string) as objects_with_affiliation_strings,
    COUNTIF(has_abstract) as objects_with_abstract,
    COUNTIF(has_citations) as objects_with_citations,
    COUNTIF(has_references) as objects_with_references,
    COUNTIF(num_fields > 1) as objects_with_more_than_one_field,

    COUNTIF(doi_not_canonical_family) as doi_not_canonical_family

FROM {table}
GROUP BY Year, type, field
ORDER BY Year DESC, type ASC, field ASC
