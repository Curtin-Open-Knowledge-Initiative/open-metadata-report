"""
Main Location for Storing Parameters for Report
"""

import datetime
from pathlib import Path
import sourceparams_openalex as openalex
import sourceparams_crossref as crossref

RERUN = False
VERBOSE = True
TODAY = datetime.date.today()
TODAY_STR = TODAY.strftime('%Y%m%d')
SOURCES = [openalex, crossref]
COMPARISON = [crossref, openalex]
SOURCE_NAMES = [source.SOURCE_NAME for source in COMPARISON]
BASE_COMPARISON = crossref
NON_BASE_SOURCES = [s for s in SOURCES if s is not BASE_COMPARISON]
SOURCES_SELF = ['dois', 'non_dois']
CURRENT = [2021, 2022, 2023]
FOCUS = 2022
# COUNT_COMPARISON = 0 #0 for comparison against base, 1 against source

# Files and Directories
SQL_DIRECTORY = Path('report_data_processing/sql')
DATA_DIR = Path('data')
# STORE_ELEMENT = {source.SOURCE_NAME: f'{source.SOURCE_NAME}_categories' for source in SOURCES}
CSV_FILE = {source.SOURCE_NAME: DATA_DIR / f'{source.SOURCE_NAME}_categories.csv' for source in SOURCES}
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

openalex.DATE = "20230122" #date of partition to use
crossref.DATE = "20230107" #date of partition to use #NB 20230107 is actually up to 20230131 (so should read 20230207)

TABLE_DATES = {source.SOURCE_NAME: source.DATE for source in SOURCES}

TABLES = {source.SOURCE_NAME: f'{source.SOURCE_TABLE_LOCATION}{source.DATE}' for source in SOURCES}

## Intermediate Tables

INTERMEDIATE_TABLES = {
    source.SOURCE_NAME:
        f'{PROJECT_ID}.{source.SOURCE_NAME}.{source.SOURCE_NAME}_intermediate{TABLE_DATES.get(source.SOURCE_NAME)}'
    for source in SOURCES
}

SOURCE_TRUTH_TABLES = {
    source.SOURCE_NAME:
        f'{PROJECT_ID}.{source.SOURCE_NAME}.{source.SOURCE_NAME}_truthtable{TABLE_DATES.get(source.SOURCE_NAME)}'
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

OPENALEX_DATA_ITEMS = [
    'authors_orcid',
    'authors_sourceid',
    'authors_string',
    'authors_sequence',
    'affiliations_countrycode',
    'affiliations_sourceid',
    'affiliations_string',
    'affiliations_ror',
    #does fields need to be included here, as it is already in CATEGORY_ITEMS ?
    'fields',
    'venue_sourceid',
    'venue_string',
    'venue_issn',
    'venue_issnl'
]

SOURCE_DATA_ITEMS = {source.SOURCE_NAME: source.SOURCE_DATA_ELEMENTS for source in SOURCES}


ALL_DATA_ITEMS = list(set(CATEGORY_DATA_ITEMS + [item for source_list in SOURCE_DATA_ITEMS.values() for item in source_list]))

SOURCE_DATA_ELEMENTS = {
}

for source in SOURCES:
    data_elements = {(elem, elem, elem) for elem in CATEGORY_DATA_ITEMS}
    data_elements = data_elements | {
        (
            # replaced 'crossref' by base source
            # elem if elem in SOURCE_DATA_ITEMS['crossref'] else CATEGORY_DATA_ITEMS[
            elem if elem in SOURCE_DATA_ITEMS[BASE_COMPARISON] else CATEGORY_DATA_ITEMS[
                CATEGORY_DATA_ITEMS.index(elem.split('_')[0])],
            elem,
            elem
        )
        for elem in SOURCE_DATA_ITEMS[source.SOURCE_NAME]
    }

    data_elements = list(data_elements)
    data_elements.sort()
    SOURCE_DATA_ELEMENTS[source] = data_elements
pass