"""
Main Location for Storing Parameters for Report
"""

import datetime
from pathlib import Path

RERUN = False
VERBOSE = True
TODAY = datetime.date.today()
TODAY_STR = TODAY.strftime('%Y%m%d')
SOURCES = ['openalex', 'crossref']
MAG_FORMAT_SOURCES = [s for s in ['mag'] if s in SOURCES]
BASE_COMPARISON = 'crossref'
NON_BASE_SOURCES = [s for s in SOURCES if s is not BASE_COMPARISON]
SOURCES_SELF = ['dois', 'non_dois']
CURRENT = [2020, 2021, 2022]
FOCUS = 2022

# Files and Directories
SQL_DIRECTORY = Path('report_data_processing/sql')
DATA_DIR = Path('data')
LOCAL_DATA_FILE = 'local_data.hd5'
LOCAL_DATA_PATH = DATA_DIR / LOCAL_DATA_FILE
STORE_ELEMENT = {source: f'{source}_categories' for source in SOURCES}
CSV_FILE = {source: DATA_DIR / f'{source}_categories.csv' for source in SOURCES}
ARCHIVE_DIR = Path('reports')

n = 1
output_store_path = ARCHIVE_DIR / f'run_{TODAY_STR}_1'
output_store_dir = f'run_{TODAY_STR}_{str(n)}'
while output_store_path.exists():
    output_store_dir = f'run_{TODAY_STR}_{str(n)}'
    output_store_path = ARCHIVE_DIR / output_store_dir
    n = n + 1
ARCHIVE_REPORT_DIR = output_store_path
ARCHIVE_REPORT_NAME = output_store_dir

# BigQuery Tables
PROJECT_ID = 'utrecht-university'
WRITE_DISPOSITION = 'WRITE_TRUNCATE'

MAG_DATE = "" #add date of partition when mag is source
OPENALEX_DATE = "20221016" #date of partition to use
CROSSREF_DATE = "20220907" #date of partition to use

MAG_TABLE_LOCATION = 'academic-observatory.mag'
OPENALEX_TABLE_LOCATION = 'academic-observatory.openalex'
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
               'Author_snapshots',
               'Concept_snapshots',
               'Institution_snapshots',
               'Venue_snapshots',
               'Work_snapshots'
               ]

TABLE_DATES = dict(mag=MAG_DATE,
                   openalex=OPENALEX_DATE,
                   crossref=CROSSREF_DATE)
TABLE_LOCATIONS = dict(mag=MAG_TABLE_LOCATION,
                       openalex=OPENALEX_TABLE_LOCATION,
                       crossref=DOI_TABLE_LOCATION)

ADDITIONAL_SOURCE_JOURNAL_FIELDS = dict(
    mag='',
    crossref=None,
    openalex=None
)

ADDITIONAL_SOURCE_ORG_FIELDS = dict(
    mag='',
    crossref=None,
    openalex=None
)

ADDITIONAL_TRUTHTABLE_FIELDS = dict(
    mag="""
    , CASE
        WHEN CHAR_LENGTH(journal.Issn) > 0
        THEN TRUE
        ELSE FALSE
        END
    as has_venue_issn,
    CASE
        WHEN CHAR_LENGTH(journal.Issn) > 0
        THEN 0
        ELSE 1
        END
    as count_venue_issn
    """,
    crossref=None,
    openalex=None
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
        additional_source_journal_fields=ADDITIONAL_SOURCE_JOURNAL_FIELDS[source],
        additional_source_org_fields=ADDITIONAL_SOURCE_ORG_FIELDS[source],
        additional_truthtable_fields=ADDITIONAL_TRUTHTABLE_FIELDS[source]
    )
    )

TABLES.update(dict(crossref=f'{DOI_TABLE_LOCATION}{CROSSREF_DATE}'))

## Intermediate Tables

INTERMEDIATE_TABLES = {
    source: f'{PROJECT_ID}.{source}.{source}_intermediate{TABLE_DATES.get(source)}'
    for source in SOURCES
}

SOURCE_TRUTH_TABLES = {
    source: f'{PROJECT_ID}.{source}.{source}_truthtable{TABLE_DATES.get(source)}'
    for source in SOURCES
}

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
    'affiliations_ror',
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
    openalex=OPENALEX_DATA_ITEMS
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

    # data_elements = data_elements | {
    #     (
    #         elem,
    #         elem if elem in SOURCE_DATA_ITEMS[source] else CATEGORY_DATA_ITEMS[
    #             CATEGORY_DATA_ITEMS.index(elem.split('_')[0])],
    #         elem
    #     )
    #     for elem in CROSSREF_DATA_ITEMS
    # }
    data_elements = list(data_elements)
    data_elements.sort()
    SOURCE_DATA_ELEMENTS[source] = data_elements