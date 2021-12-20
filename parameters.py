"""
Main Location for Storing Parameters for Report
"""

RERUN = True
VERBOSE = True

PROJECT_ID = 'utrecht-university'

# BigQuery Tables

SOURCES = ['mag', 'openalex']

MAG_DATE = "20211011"
OPENALEX_DATE = "20211011"

MAG_TABLE_LOCATION = 'academic-observatory.mag'
OPENALEX_TABLE_LOCATION = 'utrecht-university.OpenAlex'

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
               'PaperMeSH'
               ]

TABLE_DATES = dict(mag=MAG_DATE, openalex=OPENALEX_DATE)
TABLE_LOCATIONS = dict(mag=MAG_TABLE_LOCATION, openalex=OPENALEX_TABLE_LOCATION)

TABLES = {
    source: {
        {
            table_name: f'{TABLE_LOCATIONS.get(source)}.{table_name}{TABLE_DATES.get(source)}'
            for table_name in TABLE_NAMES
        }
    } for source in SOURCES
}

DOIS_ONLY_SELECTOR = {
    source: f"""
FROM 
    (
    SELECT 
        UPPER(TRIM(doi)), 
        ARRAY_AGG(Paperid ORDER BY CitationCount DESC)[offset(0)] as PaperId		
    FROM `{TABLES[source].get('Papers')}` as papers		
    WHERE papers.doi IS NOT NULL		
    GROUP BY UPPER(TRIM(doi))
    ) 
    as dois
"""
    for source in SOURCES
}

ALL_OBJECTS_SELECTOR = {
    source: f"""FROM `{TABLES[source].get('Papers')}` as papers""" for source in SOURCES
}
