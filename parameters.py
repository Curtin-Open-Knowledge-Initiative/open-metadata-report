"""
Main Location for Storing Parameters for Report
"""

import datetime

RERUN = False
VERBOSE = True
TODAY = datetime.date.today()
TODAY_STR = TODAY.strftime('%Y%m%d')

# Files and Directories
SQL_DIRECTORY = 'report_data_processing/sql'
LOCAL_DATA = 'local_data.hd5'

# BigQuery Tables
PROJECT_ID = 'utrecht-university'
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

OPEN_ALEX_ADDITIONAL_FIELDS = dict(
    mag='null as RorId, null as Orcid, ',
    crossref=None,
    openalex='affiliation.RorId, author.Orcid, '
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
        openalex_additional_fields=OPEN_ALEX_ADDITIONAL_FIELDS[source]
    ))

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

## Quasi DOI Table

Q_DOI_TABLE = f'{PROJECT_ID}.crossref.crossref_intermediate{TABLE_DATES.get("crossref")}'

## Crossref Member Data Table

CROSSREF_MEMBER_DATA_TABLE = f'{PROJECT_ID}.crossref.member_data'

## Category Queries Metadata

CATEGORY_DATA_ITEMS = [
    'authors',
    'affiliation_id',
    'gridid',
    'rorid',
    'orcid',
    'affiliation_string',
    'abstract',
    'citations',
    'references',
    'fields'
]
