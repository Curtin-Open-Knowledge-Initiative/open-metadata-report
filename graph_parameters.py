from pathlib import Path
from data_parameters import ALL_DATA_ITEMS, SOURCES

BASE_COMPARISON = 'crossref'
GRAPH_DIR = Path('graphs')
FORMATTED_SOURCE_NAMES = dict(
    crossref='Crossref',
    mag='MAG',
    openalex='OpenAlex (MAG format)',
    openalex_native='OpenAlex'
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
            'xs': ['Affiliation strings', 'Authors', 'Abstracts', 'Citations to',
                   'References from', 'Open References from',
                   'Journals', 'Journals ISSN', 'Fields'],
            'ys': {
                'Crossref': {
                    'Affiliation strings': 'pc_crossref_has_affiliations_string',
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
                    'Affiliation strings': 'pc_mag_has_affiliations_string',
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
                    'Affiliation strings': 'pc_mag_affiliations_string_adds_presence',
                    'Authors': 'pc_mag_authors_adds_presence',
                    'Abstracts': 'pc_mag_abstract_adds_presence',
                    'Citations to': 'pc_mag_citations_adds_presence',
                    'References from': 'pc_mag_references_adds_presence',
                    'Open References from': 'pc_mag_references_adds_presence',
                    'Journals': 'pc_mag_venue_adds_presence',
                    'Journals ISSN': 'pc_mag_has_venue_issn_adds_presence',
                    'Fields': 'pc_mag_fields_adds_presence'
                }
            }
        },
        'openalex': {
            'xs': ['Affiliation strings', 'Authors', 'Authors ORCIDs', 'Abstracts', 'Citations to',
                   'References from', 'Open References from',
                   'Journals', 'Journals ISSN', 'Fields'],
            'ys': {
                'Crossref': {
                    'Affiliation strings': 'pc_crossref_has_affiliations_string',
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
                    'Affiliation strings': 'pc_openalex_has_affiliations_string',
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
                    'Affiliation strings': 'pc_openalex_affiliations_string_adds_presence',
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
            'xs': ['Affiliation strings', 'Authors', 'Authors ORCIDs', 'Abstracts', 'Citations to',
                   'References from', 'Open References from',
                   'Journals', 'Journals ISSN', 'Fields'],
            'ys': {
                'Crossref': {
                    'Affiliation strings': 'pc_crossref_has_affiliations_string',
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
                    'Affiliation strings': 'pc_openalex_native_has_affiliations_string',
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
                    'Affiliation strings': 'pc_openalex_native_affiliations_string_adds_presence',
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
    }
}

STACKED_BAR_SUMMARY_XS = ['Affiliation strings', 'Authors', 'Abstracts', 'Citations to', 'References from',
                          'Journals']

SIDEBYSIDE_BAR_SUMMARY_XS = ['Affiliation strings', 'Authors', 'Abstracts', 'Citations to', 'References from',
                             'Journals', 'Fields']

CROSSREF_TYPES = ['journal-article',
                  'proceedings-article',
                  'book-chapter',
                  'book',
                  'posted-content',
                  'report',
                  'monograph']

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
