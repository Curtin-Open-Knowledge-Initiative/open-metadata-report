SELECT
    doi,
    id as source_id,
    type,
    publication_year as published_year,

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
    as has_authors_sourceid,
    (SELECT COUNT(1) FROM UNNEST(authorships) AS authors WHERE authors.author.id is not null) as count_authors_sourceid,
    CASE
        WHEN
            (SELECT COUNT(1) FROM UNNEST(authorships) AS authors WHERE authors.author.orcid is not null) > 0 THEN TRUE
        ELSE FALSE
    END
    as has_authors_orcid,
    (SELECT COUNT(1) FROM UNNEST(authorships) AS authors WHERE authors.author.orcid is not null) as count_authors_orcid,
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
    as has_affiliations_source_id,
    (SELECT COUNT(1) FROM UNNEST(authorships) AS authors, UNNEST(institutions) as institution WHERE institution.id is not null) as count_affiliations_sourceid,
    CASE
        WHEN
            (SELECT COUNT(1) FROM UNNEST(authorships) AS authors, UNNEST(institutions) as institution WHERE institution.ror is not null) > 0 THEN TRUE
        ELSE FALSE
    END
    as has_affiliations_ror,
    (SELECT COUNT(1) FROM UNNEST(authorships) AS authors, UNNEST(institutions) as institution WHERE institution.ror is not null) as count_affiliations_ror,
    CASE
        WHEN
            (SELECT COUNT(1) FROM UNNEST(authorships) AS authors, UNNEST(institutions) as institution WHERE institution.country_code is not null) > 0 THEN TRUE
        ELSE FALSE
    END
    as has_affiliations_countrycode,
    (SELECT COUNT(1) FROM UNNEST(authorships) AS authors, UNNEST(institutions) as institution WHERE institution.country_code is not null) as count_affiliations_country_code,

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
    CASE
        WHEN (SELECT COUNT(1) FROM UNNEST(concepts) AS fields WHERE fields.id is not null) > 0 THEN TRUE
        ELSE FALSE
    END
    as has_fields_mag,
    (SELECT COUNT(1) FROM UNNEST(concepts) AS fields WHERE fields.id is not null) as count_fields_mag,

    (SELECT fields.display_name from UNNEST(concepts) as fields WHERE fields.level = 0 LIMIT 1) as field,

    CASE
        WHEN (SELECT COUNT(1) FROM UNNEST(mesh) AS fields WHERE fields.descriptor_ui is not null) > 0 THEN TRUE
        ELSE FALSE
    END
    as has_fields_mesh,
    (SELECT COUNT(1) FROM UNNEST(mesh) AS fields WHERE fields.descriptor_ui is not null) as count_fields_mesh

FROM `{table}`