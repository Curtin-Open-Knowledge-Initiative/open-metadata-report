SELECT
    Doi as doi,
    PaperId as source_id,
    DocType as type,
    Year as published_year,
    ARRAY_LENGTH(authors) as count_authors,
    CASE
        WHEN (SELECT COUNT(1) FROM UNNEST(authors) AS authors WHERE authors.AffiliationId is not null) > 0 THEN TRUE
        ELSE FALSE
    END
    as has_affiliation_id,
    (SELECT COUNT(1) FROM UNNEST(authors) AS authors WHERE authors.AffiliationId is not null) as count_affiliation_id,
    CASE
        WHEN (SELECT COUNT(1) FROM UNNEST(authors) AS authors WHERE authors.GridId is not null) > 0 THEN TRUE
        ELSE FALSE
    END
    as has_gridid,
    (SELECT COUNT(1) FROM UNNEST(authors) AS authors WHERE authors.GridId is not null) as count_gridid,
    CASE
        WHEN (SELECT COUNT(1) FROM UNNEST(authors) AS authors WHERE authors.RorId is not null) > 0 THEN TRUE
        ELSE FALSE
    END
    as has_rorid,
    (SELECT COUNT(1) FROM UNNEST(authors) AS authors WHERE authors.RorId is not null) as count_rorid,
    CASE
        WHEN (SELECT COUNT(1) FROM UNNEST(authors) AS authors WHERE authors.Orcid is not null) > 0 THEN TRUE
        ELSE FALSE
    END
    as has_orcid,
    (SELECT COUNT(1) FROM UNNEST(authors) AS authors WHERE authors.Orcid is not null) as count_orcid,
    CASE
        WHEN (SELECT COUNT(1) FROM UNNEST(authors) AS authors WHERE authors.OriginalAffiliation is not null) > 0 THEN TRUE
        ELSE FALSE
    END
    as has_affiliation_string,
    (SELECT COUNT(1) FROM UNNEST(authors) AS authors WHERE authors.OriginalAffiliation is not null) as count_affiliation_string,
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
    CitationCount as count_citations,
    -- There is no equivalent of the public_references status in Crossref so we check the count
    -- This is therefore different to the equivalent term in the Crossref Truth Table
    CASE
        WHEN ReferenceCount > 0 THEN TRUE
        ELSE FALSE
    END
    as has_references,
    ReferenceCount as count_references,

    CASE
        WHEN ARRAY_LENGTH(fields.level_0) > 0
        THEN fields.level_0[OFFSET(0)].DisplayName
        ELSE null
        END
    as top_field,
--    CASE
--        WHEN ARRAY_LENGTH(fields.level_0) > 0
--        THEN ARRAY_TO_STRING((SELECT DisplayName FROM fields.level_0))
--        ELSE null
--        END
--    as fields,
    ARRAY_LENGTH(fields.level_0) as count_fields,

    CASE
        WHEN ((Doi is not null) AND (PaperId != FamilyId) AND (FamilyId is not null)) THEN TRUE
        ELSE FALSE
    END
    as doi_not_canonical_family

FROM `{table}`