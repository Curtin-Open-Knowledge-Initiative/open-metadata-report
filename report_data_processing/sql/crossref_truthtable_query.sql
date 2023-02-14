--- deduplicate DOIs on created_date
WITH table_cleaned AS (

    SELECT
        papers.*

    FROM (SELECT DOI, ARRAY_AGG(DATE(created.date_time) ORDER BY DATE(created.date_time) DESC)[offset(0)] as var_dedup
    FROM `{table}`
    GROUP BY DOI) as dois

    LEFT JOIN `{table}` as papers
    ON papers.DOI = dois.DOI
    AND DATE(papers.created.date_time) = DATE(dois.var_dedup)
)

SELECT
    UPPER(TRIM(doi)) as source_id,
    UPPER(TRIM(doi)) as doi,
    DATE(created.date_time) AS created_date,
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
        WHEN (SELECT COUNT(1) FROM UNNEST(author) AS authors, UNNEST(authors.affiliation) AS affiliation, UNNEST (affiliation.id) AS affiliation_id WHERE (affiliation_id.id is not null AND affiliation_id.id_type = 'ROR')) > 0 THEN TRUE
        ELSE FALSE
    END
    as has_affiliations_ror,
    (SELECT COUNT(1) FROM UNNEST(author) AS authors, UNNEST(authors.affiliation) AS affiliation, UNNEST (affiliation.id) AS affiliation_id WHERE (affiliation_id.id is not null AND affiliation_id.id_type = 'ROR')) as count_affiliations_ror,

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

FROM table_cleaned

