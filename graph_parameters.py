from pathlib import Path
import os

from data_parameters import ALL_DATA_ITEMS, SOURCES, SOURCES_SELF, CURRENT, FOCUS

BASE_COMPARISON = 'crossref'
GRAPH_DIR = Path('graphs')
if not GRAPH_DIR.is_dir():
    os.mkdir(GRAPH_DIR)

FORMATTED_SOURCE_NAMES = dict(
    crossref='Crossref',
    openalex='OpenAlex'
)

# Time Frames

CROSSREF_CURRENT = CURRENT
FOCUS_YEAR = FOCUS

TIME_FRAMES = {
    'All Time': range(1900, 2100),
    'Crossref Current': CROSSREF_CURRENT,
    'Focus Year': [FOCUS_YEAR]
}

# Value Add Graphs

PRESENCE_COLUMNS = [
    f'{source}_has_{item}' for item in ALL_DATA_ITEMS for source in SOURCES
]

PRESENCE_COLUMNS_SELF = [
    f'{source_self}_has_{item}' for item in ALL_DATA_ITEMS for source_self in SOURCES_SELF
]


ADDED_VALUE_COLUMNS = [
    f'{source}_{item}_adds_presence' for item in ALL_DATA_ITEMS for source in SOURCES if source is not BASE_COMPARISON
]

ALL_COLLATED_COLUMNS = PRESENCE_COLUMNS + ADDED_VALUE_COLUMNS

VALUE_ADD_META = {
    'crossref': {
        'openalex': {
            'xs': ['Affiliations', 'Affiliations ROR', 'Authors', 'Authors ORCIDs', 'Abstracts', 'Citations to',
                   'References from', 'Journals', 'Journals ISSN', 'Fields'],
            'ys': {
                'Crossref': {
                    'Affiliations': 'pc_crossref_has_affiliations_string',
                    'Affiliations ROR': 'pc_crossref_has_affiliations_ror',
                    'Authors': 'pc_crossref_has_authors',
                    'Authors ORCIDs': 'pc_crossref_has_authors_orcid',
                    'Abstracts': 'pc_crossref_has_abstract',
                    'Citations to': 'pc_crossref_has_citations',
                    'References from': 'pc_crossref_has_references',
                    'Journals': 'pc_crossref_has_venue',
                    'Journals ISSN': 'pc_crossref_has_venue_issn',
                    'Fields': 'pc_crossref_has_fields'
                },
                'OpenAlex': {
                    'Affiliations': 'pc_openalex_has_affiliations_string',
                    'Affiliations ROR': 'pc_openalex_has_affiliations_ror',
                    'Authors': 'pc_openalex_has_authors',
                    'Authors ORCIDs': 'pc_openalex_has_authors_orcid',
                    'Abstracts': 'pc_openalex_has_abstract',
                    'Citations to': 'pc_openalex_has_citations',
                    'References from': 'pc_openalex_has_references',
                    'Journals': 'pc_openalex_has_venue',
                    'Journals ISSN': 'pc_openalex_has_venue_issn',
                    'Fields': 'pc_openalex_has_fields'
                },
                'OpenAlex Added Value': {
                    'Affiliations': 'pc_openalex_affiliations_string_adds_presence',
                    'Affiliations ROR': 'pc_openalex_affiliations_ror_adds_presence',
                    'Authors': 'pc_openalex_authors_adds_presence',
                    'Authors ORCIDs': 'pc_openalex_authors_orcid_adds_presence',
                    'Abstracts': 'pc_openalex_abstract_adds_presence',
                    'Citations to': 'pc_openalex_citations_adds_presence',
                    'References from': 'pc_openalex_references_adds_presence',
                    'Journals': 'pc_openalex_venue_adds_presence',
                    'Journals ISSN': 'pc_openalex_has_venue_issn',
                    'Fields': 'pc_openalex_fields_adds_presence'
                }
            }
        }
    },
    'openalex': {
        'openalex': {
            'xs': ['Affiliations', 'Affiliations ROR', 'Authors', 'Authors ORCIDs', 'Abstracts', 'Citations to',
                   'References from', 'Journals', 'Journals ISSN', 'Fields'],
            'ys': {
                'OpenAlex DOIs': {
                    'Affiliations': 'pc_dois_has_affiliations_string',
                    'Affiliations ROR': 'pc_dois_has_affiliations_ror',
                    'Authors': 'pc_dois_has_authors',
                    'Authors ORCIDs': 'pc_dois_has_authors_orcid',
                    'Abstracts': 'pc_dois_has_abstract',
                    'Citations to': 'pc_dois_has_citations',
                    'References from': 'pc_dois_has_references',
                    'Journals': 'pc_dois_has_venue',
                    'Journals ISSN': 'pc_dois_has_venue_issn',
                    'Fields': 'pc_dois_has_fields'
                },
                'OpenAlex non-DOIs': {
                    'Affiliations': 'pc_non_dois_has_affiliations_string',
                    'Affiliations ROR': 'pc_non_dois_has_affiliations_ror',
                    'Authors': 'pc_non_dois_has_authors',
                    'Authors ORCIDs': 'pc_non_dois_has_authors_orcid',
                    'Abstracts': 'pc_non_dois_has_abstract',
                    'Citations to': 'pc_non_dois_has_citations',
                    'References from': 'pc_non_dois_has_references',
                    'Journals': 'pc_non_dois_has_venue',
                    'Journals ISSN': 'pc_non_dois_has_venue_issn',
                    'Fields': 'pc_non_dois_has_fields'
                }
            }
        }
    }
}

STACKED_BAR_SUMMARY_XS = ['Affiliations', 'Authors', 'Abstracts', 'Citations to', 'References from',
                          'Journals']

SIDEBYSIDE_BAR_SUMMARY_XS = ['Affiliations', 'Authors', 'Abstracts', 'Citations to', 'References from',
                             'Journals', 'Fields']

CROSSREF_TYPES = ['journal-article',
                  'proceedings-article',
                  'book-chapter',
                  'book',
                  'posted-content',
                  'report',
                  'monograph']

OPENALEX_TYPES = ['journal-article',
                         'proceedings-article',
                         'book-chapter',
                         'book',
                         'posted-content',
                         'report',
                         'monograph',
                         'none']


# Sources in Base Crossref Over Time

SOURCE_IN_BASE_YEAR_RANGE = range(1980, 2022)

# Tables

SUMMARY_TABLE_COLUMNS = {
    'crossref': {
        'column_names': [
            'timeframe',
            'crossref_dois',
            'crossref_has_authors',
            'crossref_has_authors_orcid',
            'crossref_has_affiliations',
            'crossref_has_affiliations_ror',
            'crossref_has_abstract',
            'crossref_has_fields',
            'crossref_has_venue',
            'crossref_has_venue_issn'],
        'nice_column_names': [
            'Time Frame',
            'Crossref DOIs',
            'Author Strings',
            'Author ORCIDs',
            'Affiliation Strings',
            'Affiliation RORs',
            'Abstracts',
            'Field Classification',
            'Venue Names',
            'ISSNs']
    },
    'openalex': {
        'column_names': [
            'timeframe',
            'crossref_dois',
            'openalex_ids'],
        'nice_column_names': [
            'Time Frame',
            'Crossref DOIs',
            'OpenAlex Coverage of DOIs'
        ]
    }
}
