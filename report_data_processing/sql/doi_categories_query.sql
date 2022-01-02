WITH
qdoi_table AS (
    SELECT *
    FROM `{qdoi_table}`
    LEFT JOIN `{crossref_member_table}`
    ON crossref.member = cr_member
    AND crossref.prefix = cr_prefix
),

truth_table AS (
    SELECT
        doi,
        crossref.type as cr_type,
        mag.DocType as mag_type,
        openalex.DocType as openalex_type,
        crossref.published_year,
        CASE
            WHEN mag.PaperId is not Null THEN TRUE
            ELSE FALSE
        END
        as has_mag_id,
        CASE
            WHEN (SELECT COUNT(1) FROM UNNEST(crossref.author) AS authors, UNNEST(authors.affiliation) AS affiliation WHERE affiliation.name is not null) > 0 THEN TRUE
            ELSE FALSE
        END
        as has_cr_affiliation_string,
        CASE
            WHEN
                (SELECT COUNT(1) from UNNEST(mag.authors) AS mauthors where mauthors.OriginalAffiliation is not null) > 0  THEN TRUE
            ELSE FALSE
        END
        as has_mag_aff_string,
        CASE
            WHEN
                (SELECT COUNT(1) FROM UNNEST(crossref.author) AS authors, UNNEST(authors.affiliation) AS affiliation WHERE affiliation.name is not null) = 0
                and
                (SELECT COUNT(1) from UNNEST(mag.authors) AS mauthors where mauthors.OriginalAffiliation is not null) > 0  THEN TRUE
            ELSE FALSE
        END
        as has_mag_aff_string_not_cr_affiliation,
        CASE
            WHEN (SELECT COUNT(1) FROM UNNEST(crossref.author) AS authors WHERE authors.authenticated_orcid is not null) > 0 THEN TRUE
            ELSE FALSE
        END
        as has_cr_authenticated_orcid,
        CASE
            WHEN (SELECT COUNT(1) FROM UNNEST(crossref.author) AS authors WHERE authors.ORCID is not null) > 0 THEN TRUE
            ELSE FALSE
        END
        as has_cr_orcid,
        CASE
            WHEN
                ((SELECT COUNT(1) FROM UNNEST(mag.authors) AS mauthors WHERE mauthors.AuthorId is not null) > 0) THEN TRUE
            ELSE FALSE
        END
        as has_mag_authorid,
        CASE
            WHEN
                ((SELECT COUNT(1) FROM UNNEST(crossref.author) AS authors WHERE authors.ORCID is not null) = 0) AND
                ((SELECT COUNT(1) FROM UNNEST(mag.authors) AS mauthors WHERE mauthors.AuthorId is not null) > 0) THEN TRUE
            ELSE FALSE
        END
        as has_mag_authorid_not_cr_orcid,
        CASE
            WHEN (SELECT COUNT(1) FROM UNNEST(crossref.author) AS authors WHERE authors.family is not null) > 0 THEN TRUE
            ELSE FALSE
        END
        as has_cr_author_name,
        CASE
            WHEN
                (SELECT COUNT(1) FROM UNNEST(mag.authors) AS mauthors WHERE mauthors.OriginalAuthor is not null) > 0 THEN TRUE
            ELSE FALSE
        END
        as has_mag_author_name,
        CASE
            WHEN
                (SELECT COUNT(1) FROM UNNEST(crossref.author) AS authors WHERE authors.family is not null) = 0
                AND
                (SELECT COUNT(1) FROM UNNEST(mag.authors) AS mauthors WHERE mauthors.OriginalAuthor is not null) > 0 THEN TRUE
            ELSE FALSE
        END
        as has_mag_not_cr_author_name,
        CASE
            WHEN (crossref.abstract is not null) THEN TRUE
            ELSE FALSE
        END
        as has_cr_abstract,
        CASE
            WHEN (mag.abstract is not null) THEN TRUE
            ELSE FALSE
        END
        as has_mag_abstract,
        CASE
            WHEN
                (crossref.abstract is null) AND
                (mag.abstract is not null) THEN TRUE
            ELSE FALSE
        END
        as has_mag_not_cr_abstract,
        CASE
            WHEN crossref.is_referenced_by_count > 0 THEN TRUE
            ELSE FALSE
        END
        as has_cr_citations,
        CASE
            WHEN (mag.CitationCount > 0) THEN TRUE
            ELSE FALSE
        END
        as has_mag_citations,
        CASE
            WHEN (crossref.is_referenced_by_count = 0) and (mag.CitationCount > 0) THEN TRUE
            ELSE FALSE
        END
        as has_mag_no_cr_citations,
        CASE
            WHEN (crossref.is_referenced_by_count = mag.CitationCount) THEN "EQUAL"
            WHEN (crossref.is_referenced_by_count > mag.CitationCount) THEN "MORE_CR"
            WHEN (crossref.is_referenced_by_count < mag.CitationCount) THEN "MORE_MAG"
            ELSE "FALSE"
        END
        as mag_vs_cr_cites,
        CASE
            WHEN crossref.references_count > 0 THEN TRUE
            ELSE FALSE
        END
        as has_cr_references,
        CASE
            WHEN (mag.ReferenceCount > 0) THEN TRUE
            ELSE FALSE
        END
        as has_mag_references,
        CASE
            WHEN (crossref.references_count = 0) and (mag.ReferenceCount > 0) THEN TRUE
            ELSE FALSE
        END
        as has_mag_no_cr_references,
        CASE
            WHEN (crossref.references_count = mag.ReferenceCount) THEN "EQUAL"
            WHEN (crossref.references_count > mag.ReferenceCount) THEN "MORE_CR"
            WHEN (crossref.references_count < mag.ReferenceCount) THEN "MORE_MAG"
            ELSE "FALSE"
        END
        as mag_vs_cr_references,
        CASE
            WHEN (crossref.references_count > 0) and (cr_ref_visibility = 'open') THEN TRUE
            ELSE FALSE
        END
        as has_cr_open_references,

        CASE
            WHEN (crossref.references_count = 0) and (mag.ReferenceCount > 0) THEN TRUE
            WHEN (crossref.references_count > 0) and (cr_ref_visibility != 'open') and (mag.ReferenceCount > 0) THEN TRUE
            ELSE FALSE
        END
        as has_mag_no_cr_open_references,

        CASE
            WHEN ARRAY_LENGTH(crossref.subject) > 0 THEN crossref.subject[OFFSET(0)]
            ELSE null
        END as
        cr_top_subject,
        CASE
            WHEN ARRAY_LENGTH(crossref.subject) > 0 THEN ARRAY_TO_STRING(crossref.subject, ";")
            ELSE null
        END as
        cr_concat_subjects,

        CASE
            WHEN ARRAY_LENGTH(crossref.subject) > 0 THEN ARRAY_LENGTH(crossref.subject)
            ELSE null
        END as num_cr_subjects,

        CASE
            WHEN (ARRAY_LENGTH(mag.fields.level_0) > 0) THEN ARRAY_LENGTH(mag.fields.level_0)
            ELSE null
        END as
        num_mag_field0,
        CASE
            WHEN (ARRAY_LENGTH(crossref.subject) = 0) AND (ARRAY_LENGTH(mag.fields.level_0) > 0) THEN TRUE
            ELSE FALSE
        END as
        has_mag_field0_not_cr_subject,

    FROM qdoi_table
)

SELECT
    published_year,
    cr_type,
    mag_type,
    COUNT(doi) as num_dois,
    COUNTIF(has_mag_id) as dois_with_mag_id,

    COUNTIF(has_cr_affiliation_string) as dois_with_cr_affiliation_strings,
    COUNTIF(has_mag_aff_string) as dois_with_mag_affiliation_strings,
    COUNTIF(has_mag_aff_string_not_cr_affiliation) as dois_mag_aff_string_but_not_cr,

    COUNTIF(has_cr_orcid) as dois_with_cr_orcid,
    COUNTIF(has_cr_authenticated_orcid) as doi_with_cr_authenticated_orcid,
    COUNTIF(has_mag_authorid) as dois_with_mag_author_id,
    COUNTIF(has_mag_authorid_not_cr_orcid) as dois_with_mag_author_id_but_not_cr_orcid,

    COUNTIF(has_cr_author_name) as dois_with_cr_author_name,
    COUNTIF(has_mag_author_name) as dois_with_mag_author_name,
    COUNTIF(has_mag_not_cr_author_name) as dois_with_mag_not_cr_author_name,

    COUNTIF(has_cr_abstract) as dois_with_cr_abstract,
    COUNTIF(has_mag_abstract) as dois_with_mag_abstract,
    COUNTIF(has_mag_not_cr_abstract) as dois_with_mag_not_cr_abstract,

    COUNTIF(has_cr_citations) as dois_with_cr_citations,
    COUNTIF(has_mag_citations) as dois_with_mag_citations,
    COUNTIF(has_mag_no_cr_citations) as dois_with_mag_not_cr_citations,
    COUNTIF(mag_vs_cr_cites = "EQUAL") as dois_same_mag_cr_citations,
    COUNTIF(mag_vs_cr_cites = "MORE_CR") as dois_more_cr_citations,
    COUNTIF(mag_vs_cr_cites = "MORE_MAG") as dois_more_mag_citations,

    COUNTIF(has_cr_references) as dois_with_cr_references,
    COUNTIF(has_mag_references) as dois_with_mag_references,
    COUNTIF(has_mag_no_cr_references) as dois_with_mag_not_cr_references,
    COUNTIF(mag_vs_cr_references = "EQUAL") as dois_same_mag_cr_references,
    COUNTIF(mag_vs_cr_references = "MORE_CR") as dois_more_cr_references,
    COUNTIF(mag_vs_cr_references = "MORE_MAG") as dois_more_mag_references,

    COUNTIF(has_cr_open_references) as dois_with_cr_open_references,
    COUNTIF(has_mag_no_cr_open_references) as dois_with_mag_not_cr_open_references,

    COUNTIF(num_cr_subjects is not null) as dois_with_cr_subjects,
    COUNTIF(num_mag_field0 is not null) as dois_with_mag_field0,
    COUNTIF(has_mag_field0_not_cr_subject) as dois_with_mag_field_not_cr_subject

FROM truth_table

GROUP BY published_year, cr_type, mag_type
ORDER BY published_year DESC, cr_type ASC, mag_type ASC