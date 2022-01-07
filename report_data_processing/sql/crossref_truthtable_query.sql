WITH
combined AS (
    SELECT *
    FROM `{table}`
    LEFT JOIN (SELECT * FROM `{crossref_member_table}` WHERE collection_date="{crossref_member_date}")
    ON crossref.member = id
    AND crossref.prefix = prefix
)

SELECT
    doi,
    crossref.type,
    crossref.published_year,
    ARRAY_LENGTH(crossref.author) as count_authors,
    CASE
        WHEN (SELECT COUNT(1) FROM UNNEST(crossref.author) AS authors, UNNEST(authors.affiliation) AS affiliation WHERE affiliation.name is not null) > 0 THEN TRUE
        ELSE FALSE
    END
    as has_affiliation_string,
    -- TODO - check when ROR IDs start appearing in Crossref metadata and allow for that to be included
    (SELECT COUNT(1) FROM UNNEST(crossref.author) AS authors, UNNEST(authors.affiliation) AS affiliation WHERE affiliation.name is not null) as count_affiliation_string,
    CASE
        WHEN (SELECT COUNT(1) FROM UNNEST(crossref.author) AS authors WHERE authors.ORCID is not null) > 0 THEN TRUE
        ELSE FALSE
    END
    as has_orcid,
    (SELECT COUNT(1) FROM UNNEST(crossref.author) AS authors WHERE authors.ORCID is not null) as count_orcid,
    CASE
        WHEN (crossref.abstract is not null) THEN TRUE
        ELSE FALSE
    END
    as has_abstract,
    CASE
        WHEN crossref.is_referenced_by_count > 0 THEN TRUE
        ELSE FALSE
    END
    as has_citations,
    crossref.is_referenced_by_count as count_citations,
    -- 'has_references' is obtained from crossref member data, not the reference count
    -- This is therefore different to the element with the same name from other sources
    public_references as has_references,
    crossref.references_count as count_references,
    CASE
        WHEN ARRAY_LENGTH(crossref.subject) > 0 THEN crossref.subject[OFFSET(0)]
        ELSE null
    END as top_field,
    CASE
        WHEN ARRAY_LENGTH(crossref.subject) > 0 THEN ARRAY_TO_STRING(crossref.subject, ";")
        ELSE null
    END as fields,

    CASE
        WHEN ARRAY_LENGTH(crossref.subject) > 0 THEN ARRAY_LENGTH(crossref.subject)
        ELSE null
    END as count_fields

FROM combined

