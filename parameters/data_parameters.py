"""
Main Location for Storing Parameters for Report
"""

import datetime
from pathlib import Path
import parameters.sourceparams_openalex as openalex
import parameters.sourceparams_crossref as crossref

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
CSV_FILE_PATHS = {source.SOURCE_NAME: DATA_DIR / f'{source.SOURCE_NAME}_categories.csv' for source in SOURCES}
CSV_FILE_PATHS.update(dict(comparison=DATA_DIR / 'comparison_categories.csv'))
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

####
#
# Data Elements by Source and Mappings
#
###

# TODO Set up set of minimial data elements here and assert they are all found in
# TODO DATA_ELEMENT_MAPPING for every source

COMPARISON_ELEMENT_MAPPING = {
}

for source_b in SOURCES:
    COMPARISON_ELEMENT_MAPPING[source_b.SOURCE_NAME] = {}
    for source_a in SOURCES:
        if source_a == source_b:
            continue
        COMPARISON_ELEMENT_MAPPING[source_b.SOURCE_NAME][source_a.SOURCE_NAME] = {}
        for element in source_b.SOURCE_DATA_ELEMENTS:
            if element in source_a.SOURCE_DATA_ELEMENTS:
                mapped_element = element
            else:
                mapped_element = "dummy_falses"
            COMPARISON_ELEMENT_MAPPING[source_b.SOURCE_NAME][source_a.SOURCE_NAME][element] = mapped_element
