WITH
fields_of_study as (
    SELECT
        fields.*,
        ARRAY(SELECT AS STRUCT
            extended.AttributeType as AttributeType,
            extended.AttributeValue as AttributeValue
         FROM `{FieldOfStudyExtendedAttributes}` as extended
         WHERE extended.FieldOfStudyId = fields.FieldOfStudyId
        ) as extended
    FROM `{FieldsOfStudy}` as fields
)

SELECT
  papers.* EXCEPT (journalId, ConferenceSeriesId, ConferenceInstanceId, CreatedDate) REPLACE ( UPPER(TRIM(Doi)) AS Doi),
  -- Note the curly braces below need to be escapes as {{ and }} due to the use of python string formatting for table names
  REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REGEXP_REPLACE(JSON_EXTRACT(IndexedAbstract, '$.InvertedIndex'), "[0-9]+", ""), ":", ""), ",", " "), '"', ""), "{{", ""), "}}", ""), "[", ""), "]", "") as abstract,
  fields.fields,
  mesh.mesh,
  authors.authors,
  STRUCT(journal.JournalId, journal.DisplayName, journal.Issn, journal.Publisher) as journal,
  STRUCT(conferenceInstance.ConferenceInstanceId,
         conferenceInstance.NormalizedName,
         conferenceInstance.DisplayName,
         conferenceInstance.Location,
         conferenceInstance.OfficialUrl,
         conferenceInstance.StartDate,
         conferenceInstance.EndDate,
         conferenceInstance.PaperCount,
         conferenceInstance.Latitude,
         conferenceInstance.Longitude
  ) as conferenceInstance,
  STRUCT(conferenceSeries.ConferenceSeriesId, conferenceSeries.NormalizedName, conferenceSeries.DisplayName) as conferenceSeries,
  extended.attributes,
  resources.resources,
  urls.urls,
  ARRAY((SELECT GridId FROM authors.authors WHERE GridId IS NOT NULL GROUP BY GridID)) as grids
FROM `{Papers}` as papers

-- Abstract
LEFT JOIN `{PaperAbstractsInvertedIndex}` as abstracts ON abstracts.PaperId = papers.PaperId

-- Journal
LEFT JOIN `{Journals}` as journal ON journal.JournalId = papers.JournalId

-- ConferenceInstance
LEFT JOIN `{ConferenceInstances}` as conferenceInstance ON conferenceInstance.ConferenceInstanceId = papers.ConferenceInstanceId

-- ConferenceSeries
LEFT JOIN `{ConferenceSeries}` as conferenceSeries ON conferenceSeries.ConferenceSeriesId = papers.ConferenceSeriesId

-- Fields of Study
LEFT JOIN (SELECT
              papers.PaperId,
              -- Fields of Study
              STRUCT(
              ARRAY_AGG(IF(fields.Level = 0, STRUCT(fields.DisplayName,fields.FieldOfStudyId,fields.Rank,fields.MainType,paperFields.Score,extended), null) IGNORE NULLS ORDER BY paperFields.Score DESC) as level_0,
              ARRAY_AGG(IF(fields.Level = 1, STRUCT(fields.DisplayName,fields.FieldOfStudyId,fields.Rank,fields.MainType,paperFields.Score,extended), null) IGNORE NULLS ORDER BY paperFields.Score DESC) as level_1,
              ARRAY_AGG(IF(fields.Level = 2, STRUCT(fields.DisplayName,fields.FieldOfStudyId,fields.Rank,fields.MainType,paperFields.Score,extended), null) IGNORE NULLS ORDER BY paperFields.Score DESC) as level_2,
              ARRAY_AGG(IF(fields.Level = 3, STRUCT(fields.DisplayName,fields.FieldOfStudyId,fields.Rank,fields.MainType,paperFields.Score,extended), null) IGNORE NULLS ORDER BY paperFields.Score DESC) as level_3,
              ARRAY_AGG(IF(fields.Level = 4, STRUCT(fields.DisplayName,fields.FieldOfStudyId,fields.Rank,fields.MainType,paperFields.Score,extended), null) IGNORE NULLS ORDER BY paperFields.Score DESC) as level_4,
              ARRAY_AGG(IF(fields.Level = 5, STRUCT(fields.DisplayName,fields.FieldOfStudyId,fields.Rank,fields.MainType,paperFields.Score,extended), null) IGNORE NULLS ORDER BY paperFields.Score DESC) as level_5) as fields
            FROM `{Papers}`  as papers
            LEFT JOIN `{PaperFieldsOfStudy}` as paperFields on papers.PaperId = paperFields.PaperId
            LEFT JOIN fields_of_study as fields on fields.FieldOfStudyId = paperFields.FieldOfStudyId
            ---WHERE papers.Doi IS NOT NULL
            GROUP BY papers.PaperId) as fields ON fields.PaperId = papers.PaperId

-- Authors
LEFT JOIN (SELECT
              papers.PaperId,
              ARRAY_AGG(STRUCT(paperAuthorAffiliations.AuthorSequenceNumber, paperAuthorAffiliations.AuthorID, paperAuthorAffiliations.OriginalAuthor, paperAuthorAffiliations.AffiliationId, paperAuthorAffiliations.OriginalAffiliation, affiliation.GridId, affiliation.Iso3166Code, affiliation.DisplayName{ openalex_additional_fields }) IGNORE NULLS ORDER BY paperAuthorAffiliations.AuthorSequenceNumber ASC) as authors
            FROM `{Papers}` as papers
            LEFT JOIN `{PaperAuthorAffiliations}` as paperAuthorAffiliations on paperAuthorAffiliations.PaperId = papers.PaperId
            LEFT JOIN `{Affiliations}` as affiliation on affiliation.AffiliationId = paperAuthorAffiliations.AffiliationId
            LEFT JOIN `{Authors}` as author on author.AuthorId = paperAuthorAffiliations.AuthorId
            GROUP BY papers.PaperId) as authors ON authors.PaperId = papers.PaperId

-- Extended Attributes
LEFT JOIN (SELECT
              PaperId,
              ARRAY_AGG(STRUCT( AttributeType, AttributeValue)) as attributes
            FROM `{PaperExtendedAttributes}`
            GROUP BY PaperId) as extended ON extended.PaperId = papers.PaperId

-- Resources
LEFT JOIN (SELECT
              PaperId,
              ARRAY_AGG(STRUCT( ResourceType , ResourceUrl )) as resources
            FROM `{PaperResources}`
            GROUP BY PaperId) as resources ON resources.PaperId = papers.PaperId

-- URLs
LEFT JOIN (SELECT
              PaperId,
              ARRAY_AGG(STRUCT( SourceType , SourceUrl, LanguageCode )) as urls
            FROM `{PaperUrls}`
            GROUP BY PaperId) as urls ON urls.PaperId = papers.PaperId

-- PaperMESH
LEFT JOIN (SELECT
              PaperId,
              ARRAY_AGG(STRUCT( DescriptorUI,	DescriptorName,	QualifierUI,	QualifierName,	IsMajorTopic )) as mesh
            FROM `{PaperMeSH}`
            GROUP BY PaperId) as mesh ON mesh.PaperId = papers.PaperId