"""
Main Location for Storing Parameters for Report
"""

import datetime
from pathlib import Path

RERUN = False
VERBOSE = True
TODAY = datetime.date.today()
TODAY_STR = TODAY.strftime('%Y%m%d')
SOURCES = ['mag', 'openalex', 'crossref', 'openalex_native']
MAG_FORMAT_SOURCES = ['mag', 'openalex']
CURRENT = [2019, 2020, 2021]

# Files and Directories
SQL_DIRECTORY = Path('report_data_processing/sql')
DATA_DIR = Path('data')
LOCAL_DATA_FILE = 'local_data.hd5'
LOCAL_DATA_PATH = DATA_DIR / LOCAL_DATA_FILE
STORE_ELEMENT = {source: f'{source}_categories' for source in SOURCES}
CSV_FILE = {source: DATA_DIR / f'{source}_categories.csv' for source in SOURCES}

# BigQuery Tables
PROJECT_ID = 'utrecht-university'
WRITE_DISPOSITION = 'WRITE_TRUNCATE'

MAG_DATE = "20211206"
OPENALEX_DATE = "20220130"
OPENALEX_NATIVE_DATE = ""
CROSSREF_DATE = "20220107"
CROSSREF_MEMBER_DATE = '2022-02-14'

MAG_TABLE_LOCATION = 'academic-observatory.mag'
OPENALEX_TABLE_LOCATION = 'utrecht-university.OpenAlex'
OPENALEX_NATIVE_TABLE_LOCATION = 'utrecht-university.OpenAlex_native'
DOI_TABLE_LOCATION = 'academic-observatory.crossref.crossref_metadata'

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
               'doi',
               'Author',
               'Concept',
               'Institution'','
               'Venue',
               'Work'
               ]

TABLE_DATES = dict(mag=MAG_DATE,
                   openalex=OPENALEX_DATE,
                   openalex_native=OPENALEX_NATIVE_DATE,
                   crossref=CROSSREF_DATE)
TABLE_LOCATIONS = dict(mag=MAG_TABLE_LOCATION,
                       openalex=OPENALEX_TABLE_LOCATION,
                       openalex_native=OPENALEX_NATIVE_TABLE_LOCATION,
                       crossref=DOI_TABLE_LOCATION)

OPENALEX_ADDITIONAL_SOURCE_FIELDS = dict(
    mag='',
    crossref=None,
    openalex=', affiliation.RorId, author.Orcid',
    openalex_native=None
)

OPENALEX_ADDITIONAL_TRUTHTABLE_FIELDS = dict(
    mag='',
    crossref=None,
    openalex="""
    , CASE
        WHEN (SELECT COUNT(1) FROM UNNEST(authors) AS authors WHERE authors.Orcid is not null) > 0 THEN TRUE
        ELSE FALSE
    END
    as has_authors_orcid
    , (SELECT COUNT(1) FROM UNNEST(authors) AS authors WHERE authors.Orcid is not null) as count_authors_orcid
    , CASE
        WHEN (SELECT COUNT(1) FROM UNNEST(authors) AS authors WHERE authors.RorId is not null) > 0 THEN TRUE
        ELSE FALSE
    END
    as has_affiliations_ror
    , (SELECT COUNT(1) FROM UNNEST(authors) AS authors WHERE authors.RorId is not null) as count_affiliations_ror
""",
    openalex_native=None
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
    'fields',
    'venue'
]

# SOURCE_DATA_ITEMS provide special classes of the standard items. These must be a subclass of a CATEGORY_DATA_ITEM
# specified in the format `categorydataitem_specialform`

CROSSREF_DATA_ITEMS = [
    'authors_orcid',
    'authors_string',
    'authors_sequence',
    'affiliations_string',
    'references_open',
    'venue_issn',
    'venue_string'
]

MAG_DATA_ITEMS = [
    'authors_sourceid',
    'authors_string',
    'authors_sequence',
    'affiliations_countrycode',
    'affiliations_sourceid',
    'affiliations_string',
    'affiliations_grid',
    'fields_mag',
    'venue_sourceid',
    'venue_string',
    'venue_issn'
]

OPENALEX_DATA_ITEMS = [
    'authors_orcid',
    'authors_sourceid',
    'authors_string',
    'authors_sequence',
    'affiliations_countrycode',
    'affiliations_sourceid',
    'affiliations_string',
    'affiliations_grid',
    'affiliations_ror',
    'fields_mag',
    'venue_sourceid',
    'venue_string',
    'venue_issn'
]

OPENALEX_NATIVE_DATA_ITEMS = [
    'authors_orcid',
    'authors_sourceid',
    'authors_string',
    'authors_sequence',
    'affiliations_countrycode',
    'affiliations_sourceid',
    'affiliations_string',
    'affiliations_ror',
    'fields_mag',
    'venue_sourceid',
    'venue_string',
    'venue_issn',
    'venue_issnl'
]

SOURCE_DATA_ITEMS = dict(
    crossref=CROSSREF_DATA_ITEMS,
    mag=MAG_DATA_ITEMS,
    openalex=OPENALEX_DATA_ITEMS,
    openalex_native=OPENALEX_NATIVE_DATA_ITEMS
)

ALL_DATA_ITEMS = list(set(CATEGORY_DATA_ITEMS + [item for source_list in SOURCE_DATA_ITEMS.values() for item in source_list]))

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
