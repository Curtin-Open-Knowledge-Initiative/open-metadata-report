"""
Main Location for Storing Parameters for Report
"""

import datetime

RERUN = True
VERBOSE = True
TODAY = datetime.date.today()
TODAY_STR = TODAY.strftime('%Y%m%d')

# Files and Directories
SQL_DIRECTORY = 'report_data_processing/sql'
LOCAL_DATA = 'local_data.hd5'

# BigQuery Tables
PROJECT_ID = 'utrecht-university'
WRITE_DISPOSITION = 'WRITE_TRUNCATE'
SOURCES = ['mag', 'openalex', 'crossref']

MAG_DATE = "20211011"
OPENALEX_DATE = "20211011"
CROSSREF_DATE = "20211002"
CROSSREF_MEMBER_DATE = '2022-01-01'

MAG_TABLE_LOCATION = 'academic-observatory.mag'
OPENALEX_TABLE_LOCATION = 'utrecht-university.OpenAlex'
DOI_TABLE_LOCATION = 'academic-observatory.observatory.doi'

TABLE_NAMES = ['Papers',
               'Affiliations',
               'Authors',
               'Journals',
               'ConferenceInstances',
               'ConferenceSeries',
               'PaperAuthorAffiliations',
               'FieldsOfStudy',
               'FieldOfStudyExtendedAttributes',
               'PaperAbstractsInvertedIndex',
               'PaperFieldsOfStudy',
               'PaperExtendedAttributes',
               'PaperResources',
               'PaperUrls',
               'PaperMeSH',
               'doi'
               ]

TABLE_DATES = dict(mag=MAG_DATE, openalex=OPENALEX_DATE, crossref=CROSSREF_DATE)
TABLE_LOCATIONS = dict(mag=MAG_TABLE_LOCATION, openalex=OPENALEX_TABLE_LOCATION, crossref=DOI_TABLE_LOCATION)

OPENALEX_ADDITIONAL_SOURCE_FIELDS = dict(
    mag='',
    crossref=None,
    openalex=', affiliation.RorId, author.Orcid'
)

OPENALEX_ADDITIONAL_TRUTHTABLE_FIELDS = dict(
    mag='',
    crossref=None,
    openalex="""
    , CASE
        WHEN (SELECT COUNT(1) FROM UNNEST(authors) AS authors WHERE authors.Orcid is not null) > 0 THEN TRUE
        ELSE FALSE
    END
    as has_authors_orcid,
    (SELECT COUNT(1) FROM UNNEST(authors) AS authors WHERE authors.Orcid is not null) as count_authors_orcid,
    CASE
        WHEN (SELECT COUNT(1) FROM UNNEST(authors) AS authors WHERE authors.RorId is not null) > 0 THEN TRUE
        ELSE FALSE
    END
    as has_affiliations_ror,
    (SELECT COUNT(1) FROM UNNEST(authors) AS authors WHERE authors.RorId is not null) as count_affiliations_ror
"""
)

TABLES = {
    source:
        {
            table_name: f'{TABLE_LOCATIONS.get(source)}.{table_name}{TABLE_DATES.get(source)}'
            for table_name in TABLE_NAMES
        }
    for source in SOURCES
}

for source in SOURCES:
    TABLES[source].update(dict(
        openalex_additional_source_fields=OPENALEX_ADDITIONAL_SOURCE_FIELDS[source],
        openalex_additional_truthtable_fields=OPENALEX_ADDITIONAL_TRUTHTABLE_FIELDS[source]
    )
    )

TABLES.update(dict(crossref=f'{DOI_TABLE_LOCATION}{CROSSREF_DATE}'))

# TODO These should probably go into the TABLES data structure
# TODO Replace all calls to INTERMEDIATE_TABLES, SOURCE_TABLES with calls to TABLES[source]['xx_table']
## Intermediate Tables

INTERMEDIATE_TABLES = {
    source: f'{PROJECT_ID}.{source}.{source}_intermediate{TABLE_DATES.get(source)}'
    for source in SOURCES
}

SOURCE_TRUTH_TABLES = {
    source: f'{PROJECT_ID}.{source}.{source}_truthtable{TABLE_DATES.get(source)}'
    for source in SOURCES
}

## Quasi DOI Table

Q_DOI_TABLE = f'{PROJECT_ID}.crossref.crossref_intermediate{TABLE_DATES.get("crossref")}'

## Crossref Member Data Table

CROSSREF_MEMBER_DATA_TABLE = f'{PROJECT_ID}.crossref.member_data'

## Category Queries Metadata

# CATEGORY_DATA_ITEMS are required to be present as both has_ and count_ items in all truth tables
# If necessary a dummy column of FALSE or 0 should be created to ensure this, but ideally this will
# provide a meaningful comparison to use as a default. count_abstract can be either an array length (eg
# for different languages or a string length)

CATEGORY_DATA_ITEMS = [
    'authors',
    'affiliations',
    'abstract',
    'citations',
    'references',
    'fields'
]

# SOURCE_DATA_ITEMS provide special classes of the standard items. These must be a subclass of a CATEGORY_DATA_ITEM
# specified in the format `categorydataitem_specialform`

CROSSREF_DATA_ITEMS = [
    'authors_orcid',
    'authors_string',
    'authors_sequence',
    'affiliations_string',
    'references_open'
]

MAG_DATA_ITEMS = [
    'authors_sourceid',
    'authors_string',
    'authors_sequence',
    'affiliations_countrycode',
    'affiliations_sourceid',
    'affiliations_string',
    'affiliations_grid',
    'fields_mag'
]

OPENALEX_DATA_ITEMS = [
    'authors_orcid', # TODO Get this into intermediate
    'authors_sourceid',
    'authors_string',
    'authors_sequence',
    'affiliations_countrycode',
    'affiliations_sourceid',
    'affiliations_string',
    'affiliations_grid',
    'affiliations_ror',
    'fields_mag'
]

SOURCE_DATA_ITEMS = dict(
    crossref=CROSSREF_DATA_ITEMS,
    mag=MAG_DATA_ITEMS,
    openalex=OPENALEX_DATA_ITEMS
)

SOURCE_DATA_ELEMENTS = {
}

for source in SOURCES:
    data_elements = {(elem, elem, elem) for elem in CATEGORY_DATA_ITEMS}
    data_elements = data_elements | {
        (
            elem if elem in SOURCE_DATA_ITEMS['crossref'] else CATEGORY_DATA_ITEMS[
                CATEGORY_DATA_ITEMS.index(elem.split('_')[0])],
            elem,
            elem
        )
        for elem in SOURCE_DATA_ITEMS[source]
    }

    data_elements = data_elements | {
        (
            elem,
            elem if elem in SOURCE_DATA_ITEMS[source] else CATEGORY_DATA_ITEMS[
                CATEGORY_DATA_ITEMS.index(elem.split('_')[0])],
            elem
        )
        for elem in CROSSREF_DATA_ITEMS
    }
    data_elements = list(data_elements)
    data_elements.sort()
    SOURCE_DATA_ELEMENTS[source] = data_elements

