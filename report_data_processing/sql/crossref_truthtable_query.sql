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
        WHEN (SELECT COUNT(1) FROM UNNEST(crossref.author) AS authors WHERE authors.ORCID is not null) > 0 THEN TRUE
        ELSE FALSE
    END as has_authors_orcid,
    (SELECT COUNT(1) FROM UNNEST(crossref.author) AS authors WHERE authors.ORCID is not null) as count_authors_orcid,
    CASE
        WHEN (SELECT COUNT(1) FROM UNNEST(crossref.author) AS authors WHERE authors.sequence is not null) > 0 THEN TRUE
        ELSE FALSE
    END as has_authors_sequence,
    (SELECT COUNT(1) FROM UNNEST(crossref.author) AS authors WHERE authors.sequence is not null) as count_authors_sequence,

    CASE
        WHEN (SELECT COUNT(1) FROM UNNEST(crossref.author) AS authors, UNNEST(authors.affiliation) AS affiliation WHERE affiliation.name is not null) > 0 THEN TRUE
        ELSE FALSE
    END
    as has_affiliations,
    (SELECT COUNT(1) FROM UNNEST(crossref.author) AS authors, UNNEST(authors.affiliation) AS affiliation WHERE affiliation.name is not null) as count_affiliations,
    CASE
        WHEN (SELECT COUNT(1) FROM UNNEST(crossref.author) AS authors, UNNEST(authors.affiliation) AS affiliation WHERE affiliation.name is not null) > 0 THEN TRUE
        ELSE FALSE
    END
    as has_affiliations_string,
    (SELECT COUNT(1) FROM UNNEST(crossref.author) AS authors, UNNEST(authors.affiliation) AS affiliation WHERE affiliation.name is not null) as count_affiliations_string,

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
    CASE
        WHEN crossref.references_count > 0 THEN TRUE
        ELSE FALSE
    END
    as has_references,
    crossref.references_count as count_references,
    CASE
        WHEN (crossref.references_count > 0) AND public_references THEN TRUE
        ELSE FALSE
    END
    as has_references_open,
    CASE
        WHEN public_references THEN crossref.references.count
        ELSE 0
    END
    as count_references_open,
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

