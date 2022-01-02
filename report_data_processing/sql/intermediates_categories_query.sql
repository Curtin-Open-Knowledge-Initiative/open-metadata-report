WITH truth_table AS (
    SELECT
        Doi,
        PaperId,
        DocType,
        Year,
        CASE
            WHEN (SELECT COUNT(1) FROM UNNEST(authors) AS authors WHERE authors.AffiliationId is not null) > 0 THEN TRUE
            ELSE FALSE
        END
        as has_affiliation_id,
        CASE
            WHEN (SELECT COUNT(1) FROM UNNEST(authors) AS authors WHERE authors.GridId is not null) > 0 THEN TRUE
            ELSE FALSE
        END
        as has_gridid,
        CASE
            WHEN (SELECT COUNT(1) FROM UNNEST(authors) AS authors WHERE authors.OriginalAffiliation is not null) > 0 THEN TRUE
            ELSE FALSE
        END
        as has_affiliation_string,
        CASE
            WHEN abstract is not null THEN TRUE
            ELSE FALSE
        END
        as has_abstract,
        CASE
            WHEN CitationCount > 0 THEN TRUE
            ELSE FALSE
        END
        as has_citations,
        CASE
            WHEN ReferenceCount > 0 THEN TRUE
            ELSE FALSE
        END
        as has_references,

        CASE
            WHEN ARRAY_LENGTH(fields.level_0) > 0
            THEN fields.level_0[OFFSET(0)].DisplayName
            ELSE null
            END
        as field,
        ARRAY_LENGTH(fields.level_0) as num_fields,

        CASE
            WHEN ((Doi is not null) AND (PaperId != FamilyId) AND (FamilyId is not null)) THEN TRUE
            ELSE FALSE
        END
        as doi_not_canonical_family

    FROM `{table}`
)

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

FROM truth_table
GROUP BY Year, type, field
ORDER BY Year DESC, type ASC, field ASC
