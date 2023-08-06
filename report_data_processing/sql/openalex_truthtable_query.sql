SELECT
    UPPER(TRIM(SUBSTRING(doi, 17))) as doi,
    id as source_id,
    type,
    publication_year as published_year,
    RANK() OVER (ORDER BY cited_by_count DESC, id DESC) as deduplication_rank,

    -- This CASE WHEN construction may be unnecessary but is consistent with the mag formatted sources
    --Authors
    CASE
        WHEN
            (SELECT COUNT(1) FROM UNNEST(authorships) AS authors WHERE authors.author.display_name is not null) > 0 THEN TRUE
        ELSE FALSE
    END
    as has_authors,
    (SELECT COUNT(1) FROM UNNEST(authorships) AS authors WHERE authors.author.display_name is not null) as count_authors,
    CASE
        WHEN
            (SELECT COUNT(1) FROM UNNEST(authorships) AS authors WHERE authors.author.display_name is not null) > 0 THEN TRUE
        ELSE FALSE
    END
    as has_authors_string,
    (SELECT COUNT(1) FROM UNNEST(authorships) AS authors WHERE authors.author.display_name is not null) as count_authors_string,
    CASE
        WHEN
            (SELECT COUNT(1) FROM UNNEST(authorships) AS authors WHERE authors.author.id is not null) > 0 THEN TRUE
        ELSE FALSE
    END
    as has_authors_id_source,
    (SELECT COUNT(1) FROM UNNEST(authorships) AS authors WHERE authors.author.id is not null) as count_authors_id_source,
    CASE
        WHEN
            (SELECT COUNT(1) FROM UNNEST(authorships) AS authors WHERE authors.author.orcid is not null) > 0 THEN TRUE
        ELSE FALSE
    END
    as has_authors_id_orcid,
    (SELECT COUNT(1) FROM UNNEST(authorships) AS authors WHERE authors.author.orcid is not null) as count_authors_id_orcid,
    CASE
        WHEN
            (SELECT COUNT(1) FROM UNNEST(authorships) AS authors WHERE authors.author_position is not null) > 0 THEN TRUE
        ELSE FALSE
    END
    as has_authors_sequence,
    (SELECT COUNT(1) FROM UNNEST(authorships) AS authors WHERE authors.author_position is not null) as count_authors_sequence,

    -- Institutions
    CASE
        WHEN
            (SELECT COUNT(1) FROM UNNEST(authorships) AS authors, UNNEST(institutions) as institution WHERE institution.display_name is not null) > 0 THEN TRUE
        ELSE FALSE
    END
    as has_affiliations,
    (SELECT COUNT(1) FROM UNNEST(authorships) AS authors, UNNEST(institutions) as institution WHERE institution.display_name is not null) as count_affiliations,
    CASE
        WHEN
            (SELECT COUNT(1) FROM UNNEST(authorships) AS authors, UNNEST(institutions) as institution WHERE institution.display_name is not null) > 0 THEN TRUE
        ELSE FALSE
    END
    as has_affiliations_string,
    (SELECT COUNT(1) FROM UNNEST(authorships) AS authors, UNNEST(institutions) as institution WHERE institution.display_name is not null) as count_affiliations_string,
    CASE
        WHEN
            (SELECT COUNT(1) FROM UNNEST(authorships) AS authors, UNNEST(institutions) as institution WHERE institution.id is not null) > 0 THEN TRUE
        ELSE FALSE
    END
    as has_affiliations_id_source,
    (SELECT COUNT(1) FROM UNNEST(authorships) AS authors, UNNEST(institutions) as institution WHERE institution.id is not null) as count_affiliations_id_source,
    CASE
        WHEN
            (SELECT COUNT(1) FROM UNNEST(authorships) AS authors, UNNEST(institutions) as institution WHERE institution.ror is not null) > 0 THEN TRUE
        ELSE FALSE
    END
    as has_affiliations_id_ror,
    (SELECT COUNT(1) FROM UNNEST(authorships) AS authors, UNNEST(institutions) as institution WHERE institution.ror is not null) as count_affiliations_id_ror,
    CASE
        WHEN
            (SELECT COUNT(1) FROM UNNEST(authorships) AS authors, UNNEST(institutions) as institution WHERE institution.country_code is not null) > 0 THEN TRUE
        ELSE FALSE
    END
    as has_affiliations_id_countrycode,
    (SELECT COUNT(1) FROM UNNEST(authorships) AS authors, UNNEST(institutions) as institution WHERE institution.country_code is not null) as count_affiliations_id_countrycode,

    -- Abstracts
    CASE
        WHEN ARRAY_LENGTH(abstract_inverted_index.keys) > 0 THEN TRUE
        ELSE FALSE
    END
    as has_abstract,
    ARRAY_LENGTH(abstract_inverted_index.keys) as count_abstract,

    -- Citations
    CASE
        WHEN cited_by_count > 0 THEN TRUE
        ELSE FALSE
    END
    as has_citations,
    cited_by_count as count_citations,

    -- References
    CASE
        WHEN ARRAY_LENGTH(referenced_works) > 0 THEN TRUE
        ELSE FALSE
    END
    as has_references,
    ARRAY_LENGTH(referenced_works) as count_references,

    -- Fields and concepts
    CASE
        WHEN (SELECT COUNT(1) FROM UNNEST(concepts) AS fields WHERE fields.id is not null) > 0 THEN TRUE
        ELSE FALSE
    END
    as has_fields,

    -- Note that this does not map to counting level 0 fields from mag format as it will count all the fields
    (SELECT COUNT(1) FROM UNNEST(concepts) AS fields WHERE fields.id is not null) as count_fields,

    (SELECT fields.display_name from UNNEST(concepts) as fields WHERE fields.level = 0 LIMIT 1) as top_field,

    -- Venue
    CASE
        WHEN primary_location.source.id is not null THEN TRUE
        ELSE FALSE
    END
    as has_venue,
    CASE
        WHEN primary_location.source.id is not null THEN 1
        ELSE 0
    END
    as count_venue,
    CASE
        WHEN primary_location.source.id is not null THEN TRUE
        ELSE FALSE
    END
    as has_venue_id_source,
    CASE
        WHEN primary_location.source.id is not null THEN 1
        ELSE 0
    END
    as count_venue_id_source,
    CASE
        WHEN CHAR_LENGTH(primary_location.source.display_name) > 0 THEN TRUE
        ELSE FALSE
    END
    as has_venue_string,
    CASE
        WHEN CHAR_LENGTH(primary_location.source.display_name) > 0 THEN 1
        ELSE 0
    END as count_venue_string,
    CASE
        WHEN ARRAY_LENGTH(primary_location.source.issn) > 0 THEN TRUE
        ELSE FALSE
    END
    as has_venue_id_issn,
    ARRAY_LENGTH(primary_location.source.issn) as count_venue_issn,
    CASE
        WHEN CHAR_LENGTH(primary_location.source.issn_l) > 0 THEN TRUE
        ELSE FALSE
    END
    as has_venue_id_issnl,
    CASE
        WHEN CHAR_LENGTH(primary_location.source.issn_l) > 0 THEN 1
        ELSE 0
    END
    as count_venue_id_issnl

    -- Funder
    CASE
        WHEN ARRAY_LENGTH(funders) > 0 THEN TRUE
        ELSE FALSE
    END as has_funders,
    ARRAY_LENGTH(funders) as count_funders,
    CASE
        WHEN (SELECT COUNT(1) FROM UNNEST(funders) AS funder WHERE funder.display_name is not null) > 0 THEN TRUE
        ELSE FALSE
    END
    as has_funders_string,
    (SELECT COUNT(1) FROM UNNEST(funders) AS funder WHERE funders.display_name is not null) as count_funders_string,
    CASE
        WHEN (SELECT COUNT(1) FROM UNNEST(funders) AS funder WHERE funder.id is not null) > 0 THEN TRUE
        ELSE FALSE
    END as has_funders_id_source,
    (SELECT COUNT(1) FROM UNNEST(funders) AS funder WHERE funder.id is not null) as count_funders_id_source,
    CASE
        WHEN (SELECT COUNT(1) FROM UNNEST(funders) AS funders, UNNEST(ids) as id WHERE id.ror is not null) > 0 THEN TRUE
        ELSE FALSE
    END as has_funders_id_ror,
    (SELECT COUNT(1) FROM UNNEST(funders) AS funder, UNNEST(ids) as id WHERE id.ror is not null) as count_funders_id_ror,


FROM `{table}`