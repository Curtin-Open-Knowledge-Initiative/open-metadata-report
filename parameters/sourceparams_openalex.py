"""
Parameters for Source OpenAlex

To create a new source, make a copy of the sourceparams_template.py file and insert what is required
"""

SOURCE_NAME = "openalex"
SOURCE_PRINT_NAME = "OpenAlex"
SOURCE_GBQ_LOCATION = "academic-observatory.openalex"
SOURCE_TABLE_NAME = "works_snapshot"
SOURCE_TABLE_LOCATION = f"{SOURCE_GBQ_LOCATION}.{SOURCE_TABLE_NAME}"

SOURCE_DATA_ELEMENTS = [
    'authors',
    'authors_id_source',
    'authors_id_orcid',
    'authors_string',
    'authors_sequence',
    'affiliations',
    'affiliations_string',
    'affiliations_id_ror',
    'affiliations_id_source',
    'affiliations_id_countrycode',
    'abstract',
    'citations',
    'references',
    'fields',
    'venue',
    'venue_string',
    'venue_id_issn',
    'venue_id_issnl',
    'venue_id_source',
    'has_funders',
    'count_funders',
    'has_funders_string',
    'count_funders_string',
    'has_funders_id_source',
    'count_funders_id_source',
    'has_funders_id_ror',
    'count_funders_id_ror',

]

