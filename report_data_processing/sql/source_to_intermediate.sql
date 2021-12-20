WITH affiliations_processed as (
  SELECT
    affiliation.AffiliationId,
    affiliation.DisplayName,
    affiliation.GridId
  FROM `{tables.get('Affiliations')}` as affiliation
),

fields_of_study as (
    SELECT
        fields.*,
        ARRAY(SELECT AS STRUCT
            extended.AttributeType as AttributeType,
            extended.AttributeValue as AttributeValue
         FROM `{tables.get('FieldOfStudyExtendedAttributes')}` as extended
         WHERE extended.FieldOfStudyId = fields.FieldOfStudyId
        ) as extended
    FROM `{tables.get('FieldsOfStudy')}` as fields
)

SELECT
  papers.* EXCEPT (journalId, ConferenceSeriesId, ConferenceInstanceId, CreatedDate) REPLACE ( UPPER(TRIM(Doi)) AS Doi),
  REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REGEXP_REPLACE(JSON_EXTRACT(IndexedAbstract, '$.InvertedIndex'), "[0-9]+", ""), ":", ""), ",", " "), '"', ""), "{", ""), "}", ""), "[", ""), "]", "") as abstract,
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
FROM `{selector}` as papers

-- Abstract
LEFT JOIN `{tables.get('PaperAbstractsInvertedIndex')}` as abstracts ON abstracts.PaperId = papers.PaperId

-- Journal
LEFT JOIN `{tables.get('Journals')}` as journal ON journal.JournalId = papers.JournalId

-- ConferenceInstance
LEFT JOIN `{tables.get('ConferenceInstances')}` as conferenceInstance ON conferenceInstance.ConferenceInstanceId = papers.ConferenceInstanceId

-- ConferenceSeries
LEFT JOIN `{tables.get('ConferenceSeries')}` as conferenceSeries ON conferenceSeries.ConferenceSeriesId = papers.ConferenceSeriesId

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
            FROM `{tables.get('Papers')}`  as papers
            LEFT JOIN `{tables.get('PaperFieldsOfStudy')}` as paperFields on papers.PaperId = paperFields.PaperId
            LEFT JOIN fields_of_study as fields on fields.FieldOfStudyId = paperFields.FieldOfStudyId
            ---WHERE papers.Doi IS NOT NULL
            GROUP BY papers.PaperId) as fields ON fields.PaperId = papers.PaperId

-- Authors
LEFT JOIN (SELECT
              papers.PaperId,
              ARRAY_AGG(STRUCT(paperAuthorAffiliations.AuthorSequenceNumber, paperAuthorAffiliations.AuthorID, paperAuthorAffiliations.OriginalAuthor, paperAuthorAffiliations.AffiliationId, paperAuthorAffiliations.OriginalAffiliation, affiliation.GridId, affiliation.DisplayName) IGNORE NULLS ORDER BY paperAuthorAffiliations.AuthorSequenceNumber ASC) as authors
            FROM `{tables.get('Papers')}` as papers
            LEFT JOIN `{tables.get('PaperAuthorAffiliations')}` as paperAuthorAffiliations on paperAuthorAffiliations.PaperId = papers.PaperId
            LEFT JOIN affiliations_processed as affiliation on affiliation.AffiliationId = paperAuthorAffiliations.AffiliationId
            GROUP BY papers.PaperId) as authors ON authors.PaperId = papers.PaperId

-- Extended Attributes
LEFT JOIN (SELECT
              PaperId,
              ARRAY_AGG(STRUCT( AttributeType, AttributeValue)) as attributes
            FROM `{tables.get('PaperExtendedAttributes')}`
            GROUP BY PaperId) as extended ON extended.PaperId = papers.PaperId

-- Resources
LEFT JOIN (SELECT
              PaperId,
              ARRAY_AGG(STRUCT( ResourceType , ResourceUrl )) as resources
            FROM `{tables.get('PaperResources')}`
            GROUP BY PaperId) as resources ON resources.PaperId = papers.PaperId

-- URLs
LEFT JOIN (SELECT
              PaperId,
              ARRAY_AGG(STRUCT( SourceType , SourceUrl, LanguageCode )) as urls
            FROM `{tables.get('PaperUrls')}`
            GROUP BY PaperId) as urls ON urls.PaperId = papers.PaperId

-- PaperMESH
LEFT JOIN (SELECT
              PaperId,
              ARRAY_AGG(STRUCT( DescriptorUI,	DescriptorName,	QualifierUI,	QualifierName,	IsMajorTopic )) as mesh
            FROM `{tables.get('PaperMeSH')}`
            GROUP BY PaperId) as mesh ON mesh.PaperId = papers.PaperId