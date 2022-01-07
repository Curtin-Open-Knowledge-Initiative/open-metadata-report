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