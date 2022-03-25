from pathlib import Path
import os

from data_parameters import ALL_DATA_ITEMS, SOURCES, SOURCES_SELF, CURRENT

BASE_COMPARISON = 'crossref'
GRAPH_DIR = Path('graphs')
if not GRAPH_DIR.is_dir():
    os.mkdir(GRAPH_DIR)

FORMATTED_SOURCE_NAMES = dict(
    crossref='Crossref',
    mag='MAG',
    openalex='OpenAlex (MAG format)',
    openalex_native='OpenAlex'
)

# Time Frames

CROSSREF_CURRENT = CURRENT
FOCUS_YEAR = 2022

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
        'mag': {
            'xs': ['Affiliations', 'Authors', 'Abstracts', 'Citations to',
                   'References from', 'Open References from',
                   'Journals', 'Journals ISSN', 'Fields'],
            'ys': {
                'Crossref': {
                    'Affiliations': 'pc_crossref_has_affiliations_string',
                    'Authors': 'pc_crossref_has_authors',
                    'Abstracts': 'pc_crossref_has_abstract',
                    'Citations to': 'pc_crossref_has_citations',
                    'References from': 'pc_crossref_has_references',
                    'Open References from': 'pc_crossref_has_references_open',
                    'Journals': 'pc_crossref_has_venue',
                    'Journals ISSN': 'pc_crossref_has_venue_issn',
                    'Fields': 'pc_crossref_has_fields'
                },
                'MAG': {
                    'Affiliations': 'pc_mag_has_affiliations_string',
                    'Authors': 'pc_mag_has_authors',
                    'Abstracts': 'pc_mag_has_abstract',
                    'Citations to': 'pc_mag_has_citations',
                    'References from': 'pc_mag_has_references',
                    'Open References from': 'pc_mag_has_references',
                    'Journals': 'pc_mag_has_venue',
                    'Journals ISSN': 'pc_mag_has_venue_issn',
                    'Fields': 'pc_mag_has_fields'
                },
                'MAG Added Value': {
                    'Affiliations': 'pc_mag_affiliations_string_adds_presence',
                    'Authors': 'pc_mag_authors_adds_presence',
                    'Abstracts': 'pc_mag_abstract_adds_presence',
                    'Citations to': 'pc_mag_citations_adds_presence',
                    'References from': 'pc_mag_references_adds_presence',
                    'Open References from': 'pc_mag_references_adds_presence',
                    'Journals': 'pc_mag_venue_adds_presence',
                    'Journals ISSN': 'pc_mag_venue_issn_adds_presence',
                    'Fields': 'pc_mag_fields_adds_presence'
                }
            }
        },
        'openalex': {
            'xs': ['Affiliations', 'Authors', 'Authors ORCIDs', 'Abstracts', 'Citations to',
                   'References from', 'Open References from',
                   'Journals', 'Journals ISSN', 'Fields'],
            'ys': {
                'Crossref': {
                    'Affiliations': 'pc_crossref_has_affiliations_string',
                    'Authors': 'pc_crossref_has_authors',
                    'Authors ORCIDs': 'pc_crossref_has_authors_orcid',
                    'Abstracts': 'pc_crossref_has_abstract',
                    'Citations to': 'pc_crossref_has_citations',
                    'References from': 'pc_crossref_has_references',
                    'Open References from': 'pc_crossref_has_references_open',
                    'Journals': 'pc_crossref_has_venue',
                    'Journals ISSN': 'pc_crossref_has_venue_issn',
                    'Fields': 'pc_crossref_has_fields'
                },
                'OpenAlex (MAG format)': {
                    'Affiliations': 'pc_openalex_has_affiliations_string',
                    'Authors': 'pc_openalex_has_authors',
                    'Authors ORCIDs': 'pc_openalex_has_authors_orcid',
                    'Abstracts': 'pc_openalex_has_abstract',
                    'Citations to': 'pc_openalex_has_citations',
                    'References from': 'pc_openalex_has_references',
                    'Open References from': 'pc_openalex_has_references',
                    'Journals': 'pc_openalex_has_venue',
                    'Journals ISSN': 'pc_openalex_has_venue_issn',
                    'Fields': 'pc_openalex_has_fields'
                },
                'OpenAlex (MAG format) Added Value': {
                    'Affiliations': 'pc_openalex_affiliations_string_adds_presence',
                    'Authors': 'pc_openalex_authors_adds_presence',
                    'Authors ORCIDs': 'pc_openalex_authors_orcid_adds_presence',
                    'Abstracts': 'pc_openalex_abstract_adds_presence',
                    'Citations to': 'pc_openalex_citations_adds_presence',
                    'References from': 'pc_openalex_references_adds_presence',
                    'Open References from': 'pc_openalex_references_adds_presence',
                    'Journals': 'pc_openalex_venue_adds_presence',
                    'Journals ISSN': 'pc_openalex_venue_issn_adds_presence',
                    'Fields': 'pc_openalex_fields_adds_presence'
                }
            },
        },
        'openalex_native': {
            'xs': ['Affiliations', 'Affiliations ROR', 'Authors', 'Authors ORCIDs', 'Abstracts', 'Citations to',
                   'References from', 'Open References from',
                   'Journals', 'Journals ISSN', 'Fields'],
            'ys': {
                'Crossref': {
                    'Affiliations': 'pc_crossref_has_affiliations_string',
                    'Affiliations ROR': 'zeros',
                    'Authors': 'pc_crossref_has_authors',
                    'Authors ORCIDs': 'pc_crossref_has_authors_orcid',
                    'Abstracts': 'pc_crossref_has_abstract',
                    'Citations to': 'pc_crossref_has_citations',
                    'References from': 'pc_crossref_has_references',
                    'Open References from': 'pc_crossref_has_references_open',
                    'Journals': 'pc_crossref_has_venue',
                    'Journals ISSN': 'pc_crossref_has_venue_issn',
                    'Fields': 'pc_crossref_has_fields'
                },
                'OpenAlex': {
                    'Affiliations': 'pc_openalex_native_has_affiliations_string',
                    'Affiliations ROR': 'pc_openalex_native_has_affiliations_ror',
                    'Authors': 'pc_openalex_native_has_authors',
                    'Authors ORCIDs': 'pc_openalex_native_has_authors_orcid',
                    'Abstracts': 'pc_openalex_native_has_abstract',
                    'Citations to': 'pc_openalex_native_has_citations',
                    'References from': 'pc_openalex_native_has_references',
                    'Open References from': 'pc_openalex_native_has_references',
                    'Journals': 'pc_openalex_native_has_venue',
                    'Journals ISSN': 'pc_openalex_native_has_venue_issn',
                    'Fields': 'pc_openalex_native_has_fields'
                },
                'OpenAlex Added Value': {
                    'Affiliations': 'pc_openalex_native_affiliations_string_adds_presence',
                    # NOTE THIS IS A HACK BECAUSE THE COMPARISON IS ZEROs (ROR not being pulled from Crossref currently)
                    # USING pc_has_affiliations_ror NOT pc___adds_presence
                    # TODO Change back when ROR from Crossref is flowing through
                    'Affiliations ROR': 'pc_openalex_native_has_affiliations_ror',
                    ###
                    'Authors': 'pc_openalex_native_authors_adds_presence',
                    'Authors ORCIDs': 'pc_openalex_native_authors_orcid_adds_presence',
                    'Abstracts': 'pc_openalex_native_abstract_adds_presence',
                    'Citations to': 'pc_openalex_native_citations_adds_presence',
                    'References from': 'pc_openalex_native_references_adds_presence',
                    'Open References from': 'pc_openalex_native_references_adds_presence',
                    'Journals': 'pc_openalex_native_venue_adds_presence',
                    'Journals ISSN': 'pc_openalex_native_has_venue_issn',
                    'Fields': 'pc_openalex_native_fields_adds_presence'
                }
            }
        }
    },
    'mag': {
        'mag': {
            'xs': ['Affiliations', 'Authors', 'Authors ORCIDs', 'Abstracts', 'Citations to',
                   'References from', 'Open References from',
                   'Journals', 'Journals ISSN', 'Fields'],
            'ys': {
                'MAG DOIs': {
                    'Affiliations': 'pc_dois_has_affiliations_string',
                    'Authors': 'pc_dois_has_authors',
                    'Authors ORCIDs': 'pc_dois_has_authors_orcid',
                    'Abstracts': 'pc_dois_has_abstract',
                    'Citations to': 'pc_dois_has_citations',
                    'References from': 'pc_dois_has_references',
                    'Open References from': 'pc_dois_has_references',
                    'Journals': 'pc_dois_has_venue',
                    'Journals ISSN': 'pc_dois_has_venue_issn',
                    'Fields': 'pc_dois_has_fields'
                },
                'MAG non-DOIs': {
                    'Affiliations': 'pc_non_dois_has_affiliations_string',
                    'Authors': 'pc_non_dois_has_authors',
                    'Authors ORCIDs': 'pc_non_dois_has_authors_orcid',
                    'Abstracts': 'pc_non_dois_has_abstract',
                    'Citations to': 'pc_non_dois_has_citations',
                    'References from': 'pc_non_dois_has_references',
                    'Open References from': 'pc_non_dois_has_references',
                    'Journals': 'pc_non_dois_has_venue',
                    'Journals ISSN': 'pc_non_dois_has_venue_issn',
                    'Fields': 'pc_non_dois_has_fields'
                }
            }
        }
    },
    'openalex': {
        'openalex': {
            'xs': ['Affiliations', 'Authors', 'Authors ORCIDs', 'Abstracts', 'Citations to',
                   'References from', 'Open References from',
                   'Journals', 'Journals ISSN', 'Fields'],
            'ys': {
                'OpenAlex (MAG format) DOIs': {
                    'Affiliations': 'pc_dois_has_affiliations_string',
                    'Authors': 'pc_dois_has_authors',
                    'Authors ORCIDs': 'pc_dois_has_authors_orcid',
                    'Abstracts': 'pc_dois_has_abstract',
                    'Citations to': 'pc_dois_has_citations',
                    'References from': 'pc_dois_has_references',
                    'Open References from': 'pc_dois_has_references',
                    'Journals': 'pc_dois_has_venue',
                    'Journals ISSN': 'pc_dois_has_venue_issn',
                    'Fields': 'pc_dois_has_fields'
                },
                'OpenAlex (MAG format) non-DOIs': {
                    'Affiliations': 'pc_non_dois_has_affiliations_string',
                    'Authors': 'pc_non_dois_has_authors',
                    'Authors ORCIDs': 'pc_non_dois_has_authors_orcid',
                    'Abstracts': 'pc_non_dois_has_abstract',
                    'Citations to': 'pc_non_dois_has_citations',
                    'References from': 'pc_non_dois_has_references',
                    'Open References from': 'pc_non_dois_has_references',
                    'Journals': 'pc_non_dois_has_venue',
                    'Journals ISSN': 'pc_non_dois_has_venue_issn',
                    'Fields': 'pc_non_dois_has_fields'
                }
            }
        }
    },
    'openalex_native': {
        'openalex_native': {
            'xs': ['Affiliations', 'Affiliations ROR', 'Authors', 'Authors ORCIDs', 'Abstracts', 'Citations to',
                   'References from', 'Open References from',
                   'Journals', 'Journals ISSN', 'Fields'],
            'ys': {
                'OpenAlex DOIs': {
                    'Affiliations': 'pc_dois_has_affiliations_string',
                    'Affiliations ROR': 'pc_dois_has_affiliations_ror',
                    'Authors': 'pc_dois_has_authors',
                    'Authors ORCIDs': 'pc_dois_has_authors_orcid',
                    'Abstracts': 'pc_dois_has_abstract',
                    'Citations to': 'pc_dois_has_citations',
                    'References from': 'pc_dois_has_references',
                    'Open References from': 'pc_dois_has_references',
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
                    'Open References from': 'pc_non_dois_has_references',
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

OPENALEX_NATIVE_TYPES = ['journal-article',
                         'proceedings-article',
                         'book-chapter',
                         'book',
                         'posted-content',
                         'report',
                         'monograph',
                         'none']

MAG_TYPES = ['Journal',
             'Conference',
             'BookChapter',
             'Book',
             'Repository',
             'Thesis']

MAG_TYPES_SELF = ['Journal',
             'Conference',
             'BookChapter',
             'Book',
             'Repository',
             'Thesis',
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
            'crossref_has_abstract',
            'crossref_has_references_open',
            'crossref_has_fields',
            'crossref_has_venue',
            'crossref_has_venue_issn'],
        'nice_column_names': [
            'Time Frame',
            'Crossref DOIs',
            'Author Strings',
            'Author ORCIDs',
            'Affiliation Strings',
            'Abstracts',
            'Open Abstracts',
            'Field Classification',
            'Venue Names',
            'ISSNs']
    },
    'mag': {
        'column_names': [
            'timeframe',
            'crossref_dois',
            'mag_ids',
            'mag_has_authors',
            'mag_has_authors_orcid',
            'mag_has_affiliations',
            'mag_has_abstract',
            'mag_has_references',
            'mag_has_fields',
            'mag_has_venue',
            'mag_has_venue_issn'],
        'nice_column_names': [
            'Time Frame',
            'Crossref DOIs',
            'MAG Coverage of DOIs',
            'Author Strings',
            'Author ORCIDs',
            'Affiliation Strings',
            'Abstracts',
            'References',
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
    },
    'openalex_native': {
        'column_names': [
            'timeframe',
            'crossref_dois',
            'openalex_native_ids'],
        'nice_column_names': [
            'Time Frame',
            'Crossref DOIs',
            'OpenAlex Coverage of DOIs'
        ]
    }
}
