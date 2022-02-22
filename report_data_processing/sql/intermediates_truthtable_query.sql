SELECT
    UPPER(TRIM(Doi)) as doi,
    PaperId as source_id,
    DocType as type,
    Year as published_year,

    -- We can't use ARRAY_LENGTH here because both mag and openalex appear to contain an empty row
    -- with nulls when there are no authors present
    CASE
        WHEN
            (SELECT COUNT(1) FROM UNNEST(authors) AS authors WHERE authors.OriginalAuthor is not null) > 0 THEN TRUE
        ELSE FALSE
    END
    as has_authors,
    (SELECT COUNT(1) FROM UNNEST(authors) AS authors WHERE authors.OriginalAuthor is not null) as count_authors,
    CASE
        WHEN
            (SELECT COUNT(1) FROM UNNEST(authors) AS authors WHERE authors.OriginalAuthor is not null) > 0 THEN TRUE
        ELSE FALSE
    END
    as has_authors_string,
    (SELECT COUNT(1) FROM UNNEST(authors) AS authors WHERE authors.OriginalAuthor is not null) as count_authors_string,
    CASE
        WHEN
            (SELECT COUNT(1) FROM UNNEST(authors) AS authors WHERE authors.AuthorId is not null) > 0 THEN TRUE
        ELSE FALSE
    END
    as has_authors_sourceid,
    (SELECT COUNT(1) FROM UNNEST(authors) AS authors WHERE authors.AuthorId is not null) as count_authors_sourceid,
    CASE
        WHEN
            (SELECT COUNT(1) FROM UNNEST(authors) AS authors WHERE authors.AuthorSequenceNumber is not null) > 0 THEN TRUE
        ELSE FALSE
    END
    as has_authors_sequence,
    (SELECT COUNT(1) FROM UNNEST(authors) AS authors WHERE authors.AuthorSequenceNumber is not null) as count_authors_sequence,

    CASE
        WHEN (SELECT COUNT(1) FROM UNNEST(authors) AS authors WHERE authors.OriginalAffiliation is not null) > 0 THEN TRUE
        ELSE FALSE
    END
    as has_affiliations,
    (SELECT COUNT(1) FROM UNNEST(authors) AS authors WHERE authors.OriginalAffiliation is not null) as count_affiliations,
    CASE
        WHEN (SELECT COUNT(1) FROM UNNEST(authors) AS authors WHERE authors.OriginalAffiliation is not null) > 0 THEN TRUE
        ELSE FALSE
    END
    as has_affiliations_string,
    (SELECT COUNT(1) FROM UNNEST(authors) AS authors WHERE authors.OriginalAffiliation is not null) as count_affiliations_string,
    CASE
        WHEN (SELECT COUNT(1) FROM UNNEST(authors) AS authors WHERE authors.AffiliationId is not null) > 0 THEN TRUE
        ELSE FALSE
    END
    as has_affiliations_sourceid,
    (SELECT COUNT(1) FROM UNNEST(authors) AS authors WHERE authors.AffiliationId is not null) as count_affiliations_sourceid,
    CASE
        WHEN (SELECT COUNT(1) FROM UNNEST(authors) AS authors WHERE authors.Iso3166Code is not null) > 0 THEN TRUE
        ELSE FALSE
    END
    as has_affiliations_countrycode,
    (SELECT COUNT(1) FROM UNNEST(authors) AS authors WHERE authors.AffiliationId is not null) as count_affiliations_countrycode,
    CASE
        WHEN (SELECT COUNT(1) FROM UNNEST(authors) AS authors WHERE authors.GridId is not null) > 0 THEN TRUE
        ELSE FALSE
    END
    as has_affiliations_grid,
    (SELECT COUNT(1) FROM UNNEST(authors) AS authors WHERE authors.GridId is not null) as count_affiliations_grid,

    CASE
        WHEN abstract is not null THEN TRUE
        ELSE FALSE
    END
    as has_abstract,
    LENGTH(abstract) as count_abstract,

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
        THEN TRUE
        ELSE FALSE
        END
    as has_fields,
    ARRAY_LENGTH(fields.level_0) as count_fields,
    CASE
        WHEN ARRAY_LENGTH(fields.level_0) > 0
        THEN TRUE
        ELSE FALSE
        END
    as has_fields_mag,
    ARRAY_LENGTH(fields.level_0) as count_fields_mag,
    CASE
        WHEN ARRAY_LENGTH(fields.level_0) > 0
        THEN fields.level_0[OFFSET(0)].DisplayName
        ELSE null
        END
    as field,

    -- Venues
    CASE
        WHEN journal.DisplayName is not null
        THEN TRUE
        ELSE FALSE
        END
    as has_venue,
    CASE
        WHEN journal.DisplayName is not null
        THEN 0
        ELSE 1
        END
    as count_venue,
    CASE
        WHEN journal.DisplayName is not null
        THEN TRUE
        ELSE FALSE
        END
    as has_venue_string,
    CASE
        WHEN journal.DisplayName is not null
        THEN 1
        ELSE 0
        END
    as count_venue_string,
    CASE
        WHEN journal.JournalId is not null
        THEN TRUE
        ELSE FALSE
        END
    as has_venue_sourceid,
    CASE
        WHEN journal.JournalId is not null
        THEN 0
        ELSE 1
        END
    as count_venue_sourceid


{additional_fields}

FROM `{table}`