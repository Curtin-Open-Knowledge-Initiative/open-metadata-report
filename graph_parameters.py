from pathlib import Path
from data_parameters import ALL_DATA_ITEMS, SOURCES

BASE_COMPARISON = 'crossref'
GRAPH_DIR = Path('graphs')
FORMATTED_SOURCE_NAMES = dict(
    crossref='Crossref',
    mag='MAG',
    openalex='OpenAlex'
)

# Time Frames

CROSSREF_CURRENT = [2019, 2020, 2021]
FOCUS_YEAR = 2020

TIME_FRAMES = {
    'All Time': range(1900, 2100),
    'Crossref Current': CROSSREF_CURRENT,
    'Focus Year': [FOCUS_YEAR]
}

# Value Add Graphs

PRESENCE_COLUMNS = [
    f'{source}_has_{item}' for item in ALL_DATA_ITEMS for source in SOURCES
]

ADDED_VALUE_COLUMNS = [
    f'{source}_{item}_adds_presence' for item in ALL_DATA_ITEMS for source in SOURCES if source is not BASE_COMPARISON
]

ALL_COLLATED_COLUMNS = PRESENCE_COLUMNS + ADDED_VALUE_COLUMNS

VALUE_ADD_META = {
    'crossref': {
        'mag': {
            'xs': ['Affiliation strings', 'Abstracts', 'Citations to', 'References from', 'Fields'],
            'ys': {
                'Crossref': {
                    'Affiliation strings': 'pc_crossref_has_affiliations_string',
                    'Abstracts': 'pc_crossref_has_abstract',
                    'Citations to': 'pc_crossref_has_citations',
                    'References from': 'pc_crossref_has_references',
                    'Fields': 'pc_crossref_has_fields'
                },
                'MAG Added Value': {
                    'Affiliation strings': 'pc_mag_affiliations_string_adds_presence',
                    'Abstracts': 'pc_mag_abstract_adds_presence',
                    'Citations to': 'pc_mag_citations_adds_presence',
                    'References from': 'pc_mag_references_adds_presence',
                    'Fields': 'pc_mag_fields_adds_presence'
                }
            }
        },
        'openalex': {
            'xs': ['Affiliation strings', 'Author ORCIDs', 'Abstracts', 'Citations to', 'References from', 'Fields'],
            'ys': {
                'Crossref': {
                    'Affiliation strings': 'pc_crossref_has_affiliations_string',
                    'Author ORCIDs': 'pc_crossref_has_authors_orcid',
                    'Abstracts': 'pc_crossref_has_abstract',
                    'Citations to': 'pc_crossref_has_citations',
                    'References from': 'pc_crossref_has_references',
                    'Fields': 'pc_crossref_has_fields'
                },
                'OpenAlex Added Value': {
                    'Affiliation strings': 'pc_openalex_affiliations_string_adds_presence',
                    'Author ORCIDs': 'pc_openalex_authors_orcid_adds_presence',
                    'Abstracts': 'pc_openalex_abstract_adds_presence',
                    'Citations to': 'pc_openalex_citations_adds_presence',
                    'References from': 'pc_openalex_references_adds_presence',
                    'Fields': 'pc_openalex_fields_adds_presence'
                }
            }
        }
    }
}

# Sources in Base Crossref Over Time

SOURCE_IN_BASE_YEAR_RANGE = range(1980, 2022)

