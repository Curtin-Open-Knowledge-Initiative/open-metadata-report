from pathlib import Path
import os

from parameters.data_parameters import SOURCES, SOURCES_SELF, CURRENT, FOCUS

GRAPH_DIR = Path('graphs')
if not GRAPH_DIR.is_dir():
    os.mkdir(GRAPH_DIR)

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

all_data_elems = [element for elems in [source.SOURCE_DATA_ELEMENTS for source in SOURCES] for element in elems]

PRESENCE_COLUMNS = [
    f'{source.SOURCE_NAME}_has_{item}' for item in all_data_elems for source in SOURCES
]

PRESENCE_COLUMNS_SELF = [
    f'{source_self}_has_{item}' for item in all_data_elems for source_self in SOURCES_SELF
]

ADDED_VALUE_COLUMNS = [
    f'{source.SOURCE_NAME}_{item}_adds_presence' for item in all_data_elems for source in SOURCES
]

ADDED_VALUE_COUNTS_COLUMNS = [
    f'{source.SOURCE_NAME}_{item}_adds_counts' for item in all_data_elems for source in SOURCES
]

ALL_COLLATED_COLUMNS = PRESENCE_COLUMNS + ADDED_VALUE_COLUMNS + ADDED_VALUE_COUNTS_COLUMNS

# TODO create values names more dynamically

# graph_print_names = {
#     'authors': 'Authors',
#     'authors_id_orcid': 'Author ORCIDs',
#     'authors_id_source': 'Author Source IDs',
#     'authors_string': 'Author Strings',
#     'affiliations_id_source': 'Affiliation Source IDs',
#     'authors_sequence': 'Authors Sequence',
#     'affiliations': 'Affiliations',
#     'affiliations_string': 'Affiliation Strings',
#     'affiliations_id_ror': 'Affiliation RORs',
#     'affiliations_id_source': 'Affiliation Source IDs',
#     'abstract': 'Abstract',
#     'citations': 'Citations',
#     'references': 'References',
#     'fields': 'Fields',
#     'venue': 'Venue',
#     'venue_string': 'Venue String',
#     'venue_id_issn': 'Venue ISSN',
#     'venue_id_issnl': 'Venue ISSN-L',
#     'venue_id_source': 'Venue Source ID'
# }

GRAPH_PRINT_NAMES = {
    'Authors': 'authors',
    'Author ORCIDs': 'authors_id_orcid',
    'Author Source IDs': 'authors_id_source',
    'Author Strings': 'authors_string',
    'Affiliation Source IDs': 'affiliations_id_source',
    'Authors Sequence': 'authors_sequence',
    'Affiliations': 'affiliations',
    'Affiliation Strings': 'affiliations_string',
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

}

value_add_meta_xs = {
    'crossref': {
        'openalex': {
            'xs': ['Affiliations', 'Affiliation RORs', 'Authors', 'Author ORCIDs', 'Abstract',
                   'Citations to', 'References from',
                   'Venue', 'Venue ISSN', 'Fields']
        },
        'openaire': {
            'xs': ['Affiliations', 'Affiliation RORs', 'Authors', 'Author ORCIDs', 'Abstract',
                   'Citations to','References from',
                   'Venue', 'Venue ISSN', 'Fields', 'Funders']
        }
    },
    'openalex': {
        'crossref': {
            'xs': ['Affiliations', 'Affiliation RORs', 'Authors', 'Author ORCIDs', 'Abstract',
                   'Citations to', 'References from',
                   'Venue', 'Venue ISSN', 'Fields']
        },
        'openaire': {
            'xs': ['Affiliations', 'Affiliation RORs', 'Authors', 'Author ORCIDs', 'Abstract',
                   'Citations to', 'References from',
                   'Venue', 'Venue ISSN', 'Fields']
        }
    },
    'openaire': {
        'crossref': {
            'xs': ['Affiliations', 'Affiliation RORs', 'Authors', 'Author ORCIDs', 'Abstract',
                   'Citations to', 'References from',
                   'Venue', 'Venue ISSN', 'Fields', 'Funders']
        },
        'openalex': {
            'xs': ['Affiliations', 'Affiliation RORs', 'Authors', 'Author ORCIDs', 'Abstract',
                   'Citations to', 'References from',
                   'Venue', 'Venue ISSN', 'Fields']
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
            x: f'pc_{source_b.SOURCE_NAME}_{GRAPH_PRINT_NAMES[x]}_adds_presence'
            for x in
            value_add_meta_xs[source_a.SOURCE_NAME][source_b.SOURCE_NAME]['xs']
        }

    }


VALUE_ADD_META = {}
for source_a in SOURCES:
    for source_b in SOURCES:
        if source_a == source_b: continue

        VALUE_ADD_META.update(
            {
                source_a.SOURCE_NAME: {
                    source_b.SOURCE_NAME: {
                        'xs': value_add_meta_xs[source_a.SOURCE_NAME][source_b.SOURCE_NAME]['xs'],
                        'ys': return_ys_dict(source_a, source_b)

                    }
                }
            }
        )

INTERNAL_COMPARISON_META = {
    'openalex': {
        'xs': ['Affiliations', 'Affiliation RORs', 'Authors', 'Author ORCIDs', 'Abstract', 'Citations to',
               'References from', 'Venue', 'Venue ISSN', 'Venue ISSN-L', 'Fields'],
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
                'Fields': 'pc_dois_has_fields'
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
                'Fields': 'pc_non_dois_has_fields'
            }
        }
    },
    'openaire': {
        'xs': ['Affiliations', 'Affiliation RORs', 'Authors', 'Author ORCIDs', 'Abstract',
               'Citations to', 'References from',
               'Venue', 'Venue ISSN', 'Venue ISSN-L', 'Fields', 'Funders', 'Funder String'],
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
                'Funder Strings': 'pc_dois_has_funders'

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
                'Funder Strings': 'pc_non_dois_has_funders',
            }
        }
    },
    'crossref': {
        'xs': ['Affiliations', 'Affiliation RORs', 'Authors', 'Author ORCIDs', 'Abstract',
               'Citations to', 'References from',
               'Venue', 'Venue ISSN', 'Fields', 'Funders', 'Funder String', 'Funder DOI'],
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

#
# VALUE_ADD_META = {
#     'crossref': {
#         'openalex': {
#             'xs': value_add_meta_xs['crossref']['openalex']['xs'],
#             'ys': {
#                 'Crossref': {
#                     x: f'pc_crossref_has_{graph_print_names[x]}'
#                     for x in
#                     value_add_meta_xs['crossref']['openalex']['xs']
#                 },
#                 'OpenAlex': {
#                     x: f'pc_openalex_has_{graph_print_names[x]}'
#                     for x in
#                     value_add_meta_xs['crossref']['openalex']['xs']
#                 },
#                 'OpenAlex Added Value': {
#                     x: f'pc_openalex_{graph_print_names[x]}_adds_presence'
#                     for x in
#                     value_add_meta_xs['crossref']['openalex']['xs']
#                 }
#             }
#         }
#     },
#     'openalex': {
#         'openalex': {
#             'xs': ['Affiliations', 'Affiliations ROR', 'Authors', 'Authors ORCIDs', 'Abstracts', 'Citations to',
#                    'References from', 'Journals', 'Journals ISSN', 'Fields'],
#             'ys': {
#                 'OpenAlex DOIs': {
#                     'Affiliations': 'pc_dois_has_affiliations_string',
#                     'Affiliations ROR': 'pc_dois_has_affiliations_ror',
#                     'Authors': 'pc_dois_has_authors',
#                     'Authors ORCIDs': 'pc_dois_has_authors_orcid',
#                     'Abstracts': 'pc_dois_has_abstract',
#                     'Citations to': 'pc_dois_has_citations',
#                     'References from': 'pc_dois_has_references',
#                     'Journals': 'pc_dois_has_venue',
#                     'Journals ISSN': 'pc_dois_has_venue_issn',
#                     'Fields': 'pc_dois_has_fields'
#                 },
#                 'OpenAlex non-DOIs': {
#                     'Affiliations': 'pc_non_dois_has_affiliations_string',
#                     'Affiliations ROR': 'pc_non_dois_has_affiliations_ror',
#                     'Authors': 'pc_non_dois_has_authors',
#                     'Authors ORCIDs': 'pc_non_dois_has_authors_orcid',
#                     'Abstracts': 'pc_non_dois_has_abstract',
#                     'Citations to': 'pc_non_dois_has_citations',
#                     'References from': 'pc_non_dois_has_references',
#                     'Journals': 'pc_non_dois_has_venue',
#                     'Journals ISSN': 'pc_non_dois_has_venue_issn',
#                     'Fields': 'pc_non_dois_has_fields'
#                 }
#             }
#         }
#     }
# }

STACKED_BAR_SUMMARY_XS = ['Affiliations', 'Authors', 'Abstract',
                          'Citations to', 'References from',
                          'Venue', 'Funders']

SIDEBYSIDE_BAR_SUMMARY_XS = ['Affiliations', 'Authors', 'Abstract',
                             'Citations to', 'References from',
                             'Venue', 'Fields', 'Funders']

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
                  'monograph',
                  'none']

OPENAIRE_TYPES = ['publication']

SOURCE_TYPES = dict(
    crossref=CROSSREF_TYPES,
    openalex=OPENALEX_TYPES,
    openaire=OPENAIRE_TYPES
)

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
