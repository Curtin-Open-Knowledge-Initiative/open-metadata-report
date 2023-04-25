"""
Parameters for Source Crossref

To create a new source, make a copy of the sourceparams_template.py file and insert what is required
"""

SOURCE_NAME = "crossref"
SOURCE_PRINT_NAME = "Crossref"
SOURCE_GBQ_LOCATION = "academic-observatory.crossref"
SOURCE_TABLE_NAME = "crossref_metadata"
SOURCE_TABLE_LOCATION = f"{SOURCE_GBQ_LOCATION}.{SOURCE_TABLE_NAME}"

SOURCE_DATA_ELEMENTS = [
    'authors',
    'authors_id_orcid',
    'authors_string',
    'authors_sequence',
    'affiliations',
    'affiliations_string',
    'affiliations_id_ror',
    'abstract',
    'citations',
    'references',
    'fields',
    'venue',
    'venue_string',
    'venue_id_issn'
]

