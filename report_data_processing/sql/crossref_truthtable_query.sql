WITH
combined AS (
    SELECT *
    FROM `{table}` as crossref
    LEFT JOIN (SELECT * FROM `{crossref_member_table}` WHERE collection_date="{crossref_member_date}") as member
    ON crossref.member = member.id
    AND crossref.prefix = member.prefix
)

SELECT
    doi as source_id,
    doi as doi,
    type,
    IF(ARRAY_LENGTH(issued.date_parts) > 0, issued.date_parts[offset(0)], null) as published_year,

    CASE
        WHEN (SELECT COUNT(1) FROM UNNEST(author) AS authors WHERE authors.family is not null) > 0 THEN TRUE
        ELSE FALSE
    END
    as has_authors,
    ARRAY_LENGTH(author) as count_authors,
    CASE
        WHEN (SELECT COUNT(1) FROM UNNEST(author) AS authors WHERE authors.family is not null) > 0 THEN TRUE
        ELSE FALSE
    END
    as has_authors_string,
    ARRAY_LENGTH(author) as count_authors_string,
    CASE
        WHEN (SELECT COUNT(1) FROM UNNEST(author) AS authors WHERE authors.ORCID is not null) > 0 THEN TRUE
        ELSE FALSE
    END as has_authors_orcid,
    (SELECT COUNT(1) FROM UNNEST(author) AS authors WHERE authors.ORCID is not null) as count_authors_orcid,
    CASE
        WHEN (SELECT COUNT(1) FROM UNNEST(author) AS authors WHERE authors.sequence is not null) > 0 THEN TRUE
        ELSE FALSE
    END as has_authors_sequence,
    (SELECT COUNT(1) FROM UNNEST(author) AS authors WHERE authors.sequence is not null) as count_authors_sequence,

    CASE
        WHEN (SELECT COUNT(1) FROM UNNEST(author) AS authors, UNNEST(authors.affiliation) AS affiliation WHERE affiliation.name is not null) > 0 THEN TRUE
        ELSE FALSE
    END
    as has_affiliations,
    (SELECT COUNT(1) FROM UNNEST(author) AS authors, UNNEST(authors.affiliation) AS affiliation WHERE affiliation.name is not null) as count_affiliations,
    CASE
        WHEN (SELECT COUNT(1) FROM UNNEST(author) AS authors, UNNEST(authors.affiliation) AS affiliation WHERE affiliation.name is not null) > 0 THEN TRUE
        ELSE FALSE
    END
    as has_affiliations_string,
    (SELECT COUNT(1) FROM UNNEST(author) AS authors, UNNEST(authors.affiliation) AS affiliation WHERE affiliation.name is not null) as count_affiliations_string,

    CASE
        WHEN (abstract is not null) THEN TRUE
        ELSE FALSE
    END
    as has_abstract,
    LENGTH(abstract) as count_abstract,

    -- Citations
    CASE
        WHEN is_referenced_by_count > 0 THEN TRUE
        ELSE FALSE
    END
    as has_citations,
    is_referenced_by_count as count_citations,

    -- References
    CASE
        WHEN references_count > 0 THEN TRUE
        ELSE FALSE
    END
    as has_references,
    references_count as count_references,
    CASE
        WHEN (references_count > 0) AND public_references THEN TRUE
        ELSE FALSE
    END
    as has_references_open,
    CASE
        WHEN public_references THEN references_count
        ELSE 0
    END
    as count_references_open,

    -- Fields
    CASE
        WHEN ARRAY_LENGTH(subject) > 0 THEN subject[OFFSET(0)]
        ELSE null
    END as top_field,
    CASE
        WHEN ARRAY_LENGTH(subject) > 0 THEN TRUE
        ELSE FALSE
    END as has_fields,
    CASE
        WHEN ARRAY_LENGTH(subject) > 0 THEN ARRAY_LENGTH(subject)
        ELSE null
    END as count_fields,

    -- Venue
    CASE
        WHEN ARRAY_LENGTH(container_title) > 0 THEN TRUE
        ELSE FALSE
        END
    as has_venue,
    ARRAY_LENGTH(container_title) as count_venue,
    CASE
        WHEN ARRAY_LENGTH(container_title) > 0 THEN TRUE
        ELSE FALSE
        END
    as has_venue_string,
    ARRAY_LENGTH(container_title) as count_venue_string,
    CASE
        WHEN ARRAY_LENGTH(ISSN) > 0 THEN TRUE
        ELSE FALSE
        END
    as has_venue_issn,
    ARRAY_LENGTH(ISSN) as count_venue_issn,

FROM combined

