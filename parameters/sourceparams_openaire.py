"""
Parameters for Source OpenAIRE

To create a new source, make a copy of the sourceparams_template.py file and insert what is required

NOTE: TODO for OpenAIRE, also tables "organization", "relation" and "project" are/will be used

"""

SOURCE_NAME = "openaire"
SOURCE_PRINT_NAME = "OpenAIRE"
SOURCE_GBQ_LOCATION = "academic-observatory.openaire"
SOURCE_TABLE_NAME = "publication"
SOURCE_TABLE_LOCATION = f"{SOURCE_GBQ_LOCATION}.{SOURCE_TABLE_NAME}"


SOURCE_DATA_ELEMENTS = [
    'authors',
    'authors_id_orcid',
    'authors_string',
    'authors_sequence',
    'affiliations',
    'affiliations_string',
    'affiliations_id_ror',
    'affiliations_id_source',
    'affiliations_id_countrycode',
    'abstract',
    'fields',
    'venue',
    'venue_string',
    'venue_id_issn',
    'venue_id_issnl'
]

