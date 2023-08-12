from pathlib import Path
import os
import itertools
import plotly

from parameters.data_parameters import SOURCES, SOURCES_SELF, COMPARISON, CURRENT, FOCUS

GRAPH_DIR = Path('graphs')
if not GRAPH_DIR.is_dir():
    os.mkdir(GRAPH_DIR)

# Palette tryout
PALETTE = plotly.colors.DEFAULT_PLOTLY_COLORS

#TO DO dynamically set colours for sources
SOURCE_PALETTE = dict(
    crossref=PALETTE[1], #safety orange #ff7f0e
    openaire=PALETTE[0], #muted blue #1f77b4
    openalex=PALETTE[2] #cooked asparagus green #2ca02c
)


# Time Frames

CROSSREF_CURRENT = CURRENT
FOCUS_YEAR = FOCUS

TIME_FRAMES = {

    'All Time': range(1980, 2023),  # NB Range does not include last number!
    # TODO align with SOURCE_IN_BASE_YEAR_RANGE
    # All time here effects value add graphs, venn graph, but not bar/line graph or coverage bar graph!
    'Crossref Current': CROSSREF_CURRENT,
    'Focus Year': [FOCUS_YEAR]
}

# Value Add Graphs

# TODO add presence and add value columns for overlap.

# only keep unique values in all_data_elems
all_data_elems = (list(set([element for elems in [source.SOURCE_DATA_ELEMENTS for source in SOURCES] for element in elems])))


PRESENCE_COLUMNS = [
    f'{source.SOURCE_NAME}_has_{item}' for item in all_data_elems for source in SOURCES
]

PRESENCE_COLUMNS_SELF = [
    f'{source_self}_has_{item}' for item in all_data_elems for source_self in SOURCES_SELF
]

ADDED_VALUE_COLUMNS_LIST = []
for source_a in SOURCES:
    for source_b in SOURCES:
        if source_a == source_b: continue

        ADDED_VALUE_COLUMNS_LIST.append(
            [f'{source_a.SOURCE_NAME}_{item}_adds_presence_{source_b.SOURCE_NAME}' for item in all_data_elems]
        )

ADDED_VALUE_COLUMNS = [element for sublist in ADDED_VALUE_COLUMNS_LIST for element in sublist]

#TODO convert this to iteration as well when counts are added back in
ADDED_VALUE_COUNTS_COLUMNS = [
    f'{source.SOURCE_NAME}_{item}_adds_counts' for item in all_data_elems for source in SOURCES
]

ALL_COLLATED_COLUMNS = PRESENCE_COLUMNS + ADDED_VALUE_COLUMNS + ADDED_VALUE_COUNTS_COLUMNS

# TODO create values names more dynamically


GRAPH_PRINT_NAMES = {
    'Authors': 'authors',
    'Author ORCIDs': 'authors_id_orcid',
    'Author Source IDs': 'authors_id_source',
    'Author Strings': 'authors_string',
    'Authors Sequence': 'authors_sequence',
    'Affiliations': 'affiliations',
    'Affiliation Strings': 'affiliations_string',
    'Affiliation Source IDs': 'affiliations_id_source',
    'Affiliation RORs': 'affiliations_id_ror',
    'Abstract': 'abstract',
    'Citations to': 'citations',
    'References from': 'references',
    'Fields': 'fields',
    'Venue': 'venue',
    'Venue String': 'venue_string',
    'Venue ISSN': 'venue_id_issn',
    'Venue ISSN-L': 'venue_id_issnl',
    'Venue Source ID': 'venue_id_source',
    'Funders': 'funders',
    'Funder Strings': 'funders_string',
    'Funder Source IDs': 'funders_id_source',
    'Funder RORs': 'funders_id_ror'
}

value_add_meta_xs = {
    'crossref': {
        'openalex': {
            'xs': ['Affiliations', 'Affiliation RORs', 'Authors', 'Author ORCIDs', 'Abstract',
                   'Citations to', 'References from', 'Venue', 'Venue ISSN', 'Fields',
                   'Funders', 'Funder Source IDs']
        },
        'openaire': {
            'xs': ['Affiliations', 'Affiliation RORs', 'Authors', 'Author ORCIDs', 'Abstract',
                   'Citations to','References from', 'Venue', 'Venue ISSN', 'Fields',
                   'Funders', 'Funder Source IDs']
        }
    },
    'openalex': {
        'crossref': {
            'xs': ['Affiliations', 'Affiliation RORs', 'Authors', 'Author ORCIDs', 'Abstract',
                   'Citations to', 'References from', 'Venue', 'Venue ISSN', 'Fields',
                   'Funders', 'Funder Strings', 'Funder Source IDs']
        },
        'openaire': {
            'xs': ['Affiliations', 'Affiliation RORs', 'Authors', 'Author ORCIDs', 'Abstract',
                   'Citations to', 'References from', 'Venue', 'Venue ISSN', 'Fields',
                   'Funders', 'Funder Strings', 'Funder Source IDs']
        }
    },
    'openaire': {
        'crossref': {
            'xs': ['Affiliations', 'Affiliation RORs', 'Authors', 'Author ORCIDs', 'Abstract',
                   'Citations to', 'References from', 'Venue', 'Venue ISSN', 'Fields',
                   'Funders', 'Funder Strings', 'Funder Source IDs']
        },
        'openalex': {
            'xs': ['Affiliations', 'Affiliation RORs', 'Authors', 'Author ORCIDs', 'Abstract',
                   'Citations to', 'References from', 'Venue', 'Venue ISSN', 'Fields',
                   'Funders', 'Funder Strings', 'Funder Source IDs']
        }
    }
}


def return_ys_dict(source_a,
                   source_b) -> dict:
    return {
        source_a.SOURCE_PRINT_NAME: {
            x: f'pc_{source_a.SOURCE_NAME}_has_{GRAPH_PRINT_NAMES[x]}'
            for x in
            value_add_meta_xs[source_a.SOURCE_NAME][source_b.SOURCE_NAME]['xs']
        },
        source_b.SOURCE_PRINT_NAME: {
            x: f'pc_{source_b.SOURCE_NAME}_has_{GRAPH_PRINT_NAMES[x]}'
            for x in
            value_add_meta_xs[source_a.SOURCE_NAME][source_b.SOURCE_NAME]['xs']
        },
        f'{source_b.SOURCE_PRINT_NAME} Added Value': {
            x: f'pc_{source_b.SOURCE_NAME}_{GRAPH_PRINT_NAMES[x]}_adds_presence_{source_a.SOURCE_NAME}'
            for x in
            value_add_meta_xs[source_a.SOURCE_NAME][source_b.SOURCE_NAME]['xs']
        }

    }


VALUE_ADD_META = {}
for source_a, source_b in itertools.permutations(SOURCES, 2):

        if not VALUE_ADD_META.get(source_a.SOURCE_NAME):
            VALUE_ADD_META[source_a.SOURCE_NAME] = {}
        VALUE_ADD_META[source_a.SOURCE_NAME][source_b.SOURCE_NAME] = dict(
                        xs=value_add_meta_xs[source_a.SOURCE_NAME][source_b.SOURCE_NAME]['xs'],
                        ys=return_ys_dict(source_a, source_b)
        )

INTERNAL_COMPARISON_META = {
    'openalex': {
        'xs': ['Affiliations', 'Affiliation RORs', 'Authors', 'Author ORCIDs', 'Abstract', 'Citations to',
               'References from', 'Venue', 'Venue ISSN', 'Venue ISSN-L', 'Fields',
               'Funders','Funder Source IDs'],
        'ys': {
            'OpenAlex DOIs': {
                'Affiliations': 'pc_dois_has_affiliations_string',
                'Affiliation RORs': 'pc_dois_has_affiliations_id_ror',
                'Authors': 'pc_dois_has_authors',
                'Author ORCIDs': 'pc_dois_has_authors_id_orcid',
                'Abstract': 'pc_dois_has_abstract',
                'Citations to': 'pc_dois_has_citations',
                'References from': 'pc_dois_has_references',
                'Venue': 'pc_dois_has_venue',
                'Venue ISSN': 'pc_dois_has_venue_id_issn',
                'Venue ISSN-L': 'pc_dois_has_venue_id_issnl',
                'Fields': 'pc_dois_has_fields',
                'Funders': 'pc_dois_has_funders',
                'Funder Source IDs': 'pc_dois_has_funders_id_source',
            },
            'OpenAlex non-DOIs': {
                'Affiliations': 'pc_non_dois_has_affiliations_string',
                'Affiliation RORs': 'pc_non_dois_has_affiliations_id_ror',
                'Authors': 'pc_non_dois_has_authors',
                'Author ORCIDs': 'pc_non_dois_has_authors_id_orcid',
                'Abstract': 'pc_non_dois_has_abstract',
                'Citations to': 'pc_non_dois_has_citations',
                'References from': 'pc_non_dois_has_references',
                'Venue': 'pc_non_dois_has_venue',
                'Venue ISSN': 'pc_non_dois_has_venue_id_issn',
                'Venue ISSN-L': 'pc_non_dois_has_venue_id_issnl',
                'Fields': 'pc_non_dois_has_fields',
                'Funders': 'pc_dois_has_funders',
                'Funder Source IDs': 'pc_dois_has_funders_id_source',
            }
        }
    },
    'openaire': {
        'xs': ['Affiliations', 'Affiliation RORs', 'Authors', 'Author ORCIDs', 'Abstract',
               'Citations to', 'References from', 'Venue', 'Venue ISSN', 'Venue ISSN-L', 'Fields',
               'Funders', 'Funder Strings'],
        'ys': {
            'OpenAIRE DOIs': {
                'Affiliations': 'pc_dois_has_affiliations_string',
                'Affiliation RORs': 'pc_dois_has_affiliations_id_ror',
                'Authors': 'pc_dois_has_authors',
                'Author ORCIDs': 'pc_dois_has_authors_id_orcid',
                'Abstract': 'pc_dois_has_abstract',
                'Citations to': 'pc_dois_has_citations',
                'References from': 'pc_dois_has_references',
                'Venue': 'pc_dois_has_venue',
                'Venue ISSN': 'pc_dois_has_venue_id_issn',
                'Venue ISSN-L': 'pc_dois_has_venue_id_issnl',
                'Fields': 'pc_dois_has_fields',
                'Funders': 'pc_dois_has_funders',
                'Funder Strings': 'pc_dois_has_funders_string'

            },
            'OpenAIRE non-DOIs': {
                'Affiliations': 'pc_non_dois_has_affiliations_string',
                'Affiliation RORs': 'pc_non_dois_has_affiliations_id_ror',
                'Authors': 'pc_non_dois_has_authors',
                'Author ORCIDs': 'pc_non_dois_has_authors_id_orcid',
                'Abstract': 'pc_non_dois_has_abstract',
                'Citations to': 'pc_non_dois_has_citations',
                'References from': 'pc_non_dois_has_references',
                'Venue': 'pc_non_dois_has_venue',
                'Venue ISSN': 'pc_non_dois_has_venue_id_issn',
                'Venue ISSN-L': 'pc_non_dois_has_venue_id_issnl',
                'Fields': 'pc_non_dois_has_fields',
                'Funders': 'pc_non_dois_has_funders',
                'Funder Strings': 'pc_non_dois_has_funders_string',
            }
        }
    },
    'crossref': {
        'xs': ['Affiliations', 'Affiliation RORs', 'Authors', 'Author ORCIDs', 'Abstract',
               'Citations to', 'References from', 'Venue', 'Venue ISSN', 'Fields',
               'Funders', 'Funder Strings', 'Funder Source IDs'],
        'ys': {
            'Crossref DOIs': {
                'Affiliations': 'pc_dois_has_affiliations_string',
                'Affiliation RORs': 'pc_dois_has_affiliations_id_ror',
                'Authors': 'pc_dois_has_authors',
                'Author ORCIDs': 'pc_dois_has_authors_id_orcid',
                'Abstract': 'pc_dois_has_abstract',
                'Citations to': 'pc_dois_has_citations',
                'References from': 'pc_dois_has_references',
                'Venue': 'pc_dois_has_venue',
                'Venue ISSN': 'pc_dois_has_venue_id_issn',
                'Fields': 'pc_dois_has_fields',
                'Funders': 'pc_dois_has_funders',
                'Funder Strings': 'pc_dois_has_funders_string',
                'Funder Source IDs': 'pc_dois_has_funders_id_source',
            },
            'Crossref non-DOIs': {
                'Affiliations': 'pc_non_dois_has_affiliations_string',
                'Affiliation RORs': 'pc_non_dois_has_affiliations_id_ror',
                'Authors': 'pc_non_dois_has_authors',
                'Author ORCIDs': 'pc_non_dois_has_authors_id_orcid',
                'Abstract': 'pc_non_dois_has_abstract',
                'Citations to': 'pc_non_dois_has_citations',
                'References from': 'pc_non_dois_has_references',
                'Venue': 'pc_non_dois_has_venue',
                'Venue ISSN': 'pc_non_dois_has_venue_id_issn',
                'Fields': 'pc_non_dois_has_fields',
                'Funders': 'pc_non_dois_has_funders',
                'Funder Strings': 'pc_non_dois_has_funders_string',
                'Funder Source IDs': 'pc_non_dois_has_funders_id_source',
            }
        }
    }
}

# These are now replaced by more comprehensive lists in value_add_meta_xs
#STACKED_BAR_SUMMARY_XS = ['Affiliations', 'Authors', 'Abstract',
#                          'Citations to', 'References from',
#                          'Venue', 'Funders']

#SIDEBYSIDE_BAR_SUMMARY_XS = ['Affiliations', 'Authors', 'Abstract',
#                             'Citations to', 'References from',
#                            'Venue', 'Fields', 'Funders']

# SOURCE_TYPES is used to specify which metadata types to include for a given source in charts by metadata type
# TODO consider moving this to source_params and call from there (but take into account using cr as default mapping for value add comparisons)
CROSSREF_TYPES = ['journal-article',
                  'proceedings-article',
                  'book-chapter',
                  'posted-content',
                  'book',
                  'report',
                  'monograph']

OPENALEX_TYPES = ['journal-article',
                  'proceedings-article',
                  'book-chapter',
                  'posted-content',
                  'book',
                  'report',
                  'monograph']
                  #'none']

OPENAIRE_TYPES = ['publication',
                  'dataset',
                  'software']
                  #'other'] remove for oria as not present in dataset

SOURCE_TYPES = dict(
    crossref=CROSSREF_TYPES,
    openalex=OPENALEX_TYPES,
    openaire=OPENAIRE_TYPES
)

# Tables - currently not used, expand when reintroduced in template report
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
    # TODO reconsider this as it presupposes comparison with Crossref - needs generalizing
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
