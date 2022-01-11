WITH
combined AS (
    SELECT *
    FROM `{table}`
    LEFT JOIN (SELECT * FROM `{crossref_member_table}` WHERE collection_date="{crossref_member_date}")
    ON crossref.member = id
    AND crossref.prefix = prefix
)

SELECT
    doi as source_id,
    doi,
    crossref.type,
    crossref.published_year,
    CASE
        WHEN (SELECT COUNT(1) FROM UNNEST(crossref.author) AS authors WHERE authors.family is not null) > 0 THEN TRUE
        ELSE FALSE
    END
    as has_authors,
    ARRAY_LENGTH(crossref.author) as count_authors,
    CASE
        WHEN (SELECT COUNT(1) FROM UNNEST(crossref.author) AS authors, UNNEST(authors.affiliation) AS affiliation WHERE affiliation.name is not null) > 0 THEN TRUE
        ELSE FALSE
    END
    as has_affiliation_string,
    (SELECT COUNT(1) FROM UNNEST(crossref.author) AS authors, UNNEST(authors.affiliation) AS affiliation WHERE affiliation.name is not null) as count_affiliation_string,
    -- TODO - check when ROR IDs start appearing in Crossref metadata and allow for that to be included
    (SELECT(FALSE)) as has_affiliation_id,
    (SELECT(0)) as count_affiliation_id,
    (SELECT(FALSE)) as has_gridid,
    (SELECT(0)) as count_gridid,
    (SELECT(FALSE)) as has_rorid,
    (SELECT(0)) as count_rorid,
    CASE
        WHEN (SELECT COUNT(1) FROM UNNEST(crossref.author) AS authors WHERE authors.ORCID is not null) > 0 THEN TRUE
        ELSE FALSE
    END as has_orcid,
    (SELECT COUNT(1) FROM UNNEST(crossref.author) AS authors WHERE authors.ORCID is not null) as count_orcid,
    CASE
        WHEN (crossref.abstract is not null) THEN TRUE
        ELSE FALSE
    END
    as has_abstract,
    LENGTH(crossref.abstract) as count_abstract,
    CASE
        WHEN crossref.is_referenced_by_count > 0 THEN TRUE
        ELSE FALSE
    END
    as has_citations,
    crossref.is_referenced_by_count as count_citations,
    -- 'has_references' is obtained from crossref member data, not the reference count
    -- This is therefore different to the element with the same name from other sources
    CASE
        WHEN (crossref.references_count > 0) AND public_references THEN TRUE
        ELSE FALSE
    END
    as has_references,
    crossref.references_count as count_references,
    CASE
        WHEN ARRAY_LENGTH(crossref.subject) > 0 THEN crossref.subject[OFFSET(0)]
        ELSE null
    END as top_field,
    CASE
        WHEN ARRAY_LENGTH(crossref.subject) > 0 THEN TRUE
        ELSE FALSE
    END as has_fields,

    CASE
        WHEN ARRAY_LENGTH(crossref.subject) > 0 THEN ARRAY_LENGTH(crossref.subject)
        ELSE null
    END as count_fields

FROM combined

