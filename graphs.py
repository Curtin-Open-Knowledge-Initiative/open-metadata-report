# Reporting template
#
# Copyright 2020-21 ######
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Authors: COKI Team, Cameron Neylon and Bianca Kramer

import json
from pathlib import Path

import pandas as pd
import numpy as np
import plotly.graph_objects as go
from typing import Optional, Callable, Union
from precipy.analytics_function import AnalyticsFunction

from observatory.reports import report_utils
from data_parameters import *
from graph_parameters import *
from report_graphs import ValueAddBar, ValueAddByCrossrefType, OverallCoverage, BarLine, Alluvial


def value_add_graphs(af: AnalyticsFunction,
                     source: str,
                     base_comparison: str = 'crossref'):
    """
    Generate graphs that provide information on the value add of a source compared to base_comparison

    :param af: AnalyticsFunction for the precipy run
    :param source: Lowercase string name of the source being compared
    :param base_comparison: Lowercase string name of the base_comparison, crossref is the default
    """

    with pd.HDFStore(LOCAL_DATA_PATH) as store:
        base_comparison_data = store[STORE_ELEMENT[base_comparison]]

    for source in SOURCES:
        if source == base_comparison:
            continue

        for timeframe in TIME_FRAMES.keys():
            filtered_sum = base_comparison_data[base_comparison_data.published_year.isin(TIME_FRAMES[timeframe])].sum(axis=0)
            figdata = collate_value_add_values(filtered_sum, ALL_COLLATED_COLUMNS)

            chart = ValueAddBar(df=figdata,
                                categories=[FORMATTED_SOURCE_NAMES[base_comparison],
                                            f'{FORMATTED_SOURCE_NAMES[source]} Added Value'],
                                xs=VALUE_ADD_META[base_comparison][source]['xs'],
                                ys=VALUE_ADD_META[base_comparison][source]['ys'])

            fig = chart.plotly()
            filename = f'value_add_{source}_{timeframe.lower().replace(" ", "_")}'
            filepath = GRAPH_DIR / filename
            fig.write_image(filepath.with_suffix('.png'))
            af.add_existing_file(filepath.with_suffix('.png'))

        # write_plotly_div(af, fig, filename + 'html')

        # chart = ValueAddBar(df=summary_table[summary_table['Time Period'] == time_period],
        #                     categories=['Crossref', 'MAG added value'],
        #                     xs=['Subjects'],
        #                     stackedbar=False)
        # fig = chart.plotly()
        # filename = f'value_add_subject_{time_period.lower().replace(" ", "_")}.'
        # fig.write_image(GRAPH_DIR / filename + 'png')
        # af.add_existing_file(GRAPH_DIR / filename + 'png')
        # write_plotly_div(af, fig, filename + 'html')


def collate_value_add_values(df: pd.DataFrame,
                             cols: list,
                             total_column: str = 'crossref_dois'):
    """
    Convenience function for cleaning up the value add tables
    :param df: summed data frame from the doi_table_categories_query
    :param cols: type: list set of columns to calculate percentages for
    :return df: type: pd.DataFrame modified dataframe with percentages calculated and all columns remaining
    """

    if type(df) == pd.Series:
        df = pd.DataFrame(df).transpose()

    for col in cols:
        if col in df.columns:
            df[f'pc_{col}'] = np.round(df[col] / df['crossref_dois'] * 100, 1)

    return df


# def alluvial_graph(af: AnalyticsFunction):
#     cr_data = load_cache_data(af,
#                               function_name=get_doi_table_data,
#                               element='doi_categories',
#                               filename=CR_DATA_FILENAME)
#     cr_data_with_nulls = cr_data.replace(to_replace={'cr_type': {
#         None: 'no assigned Crossref Type'
#     },
#         'mag_type': {
#             None: 'no assigned MAG Type'
#         }
#     }
#     )
#
#     figdata = cr_data_with_nulls.groupby(['cr_type', 'mag_type']).agg(
#         num_dois=pd.NamedAgg(column='num_dois', aggfunc='sum')
#     )
#
#     cr_order = ['journal-article', 'book-chapter', 'proceedings-article', 'dataset',
#                 'book', 'journal-issue', 'reference-entry', 'posted-content', 'report',
#                 'monograph', 'component', 'proceedings', 'report-series', 'book-section',
#                 'book-part', 'standard', 'book-track', 'other', 'no assigned Crossref Type']
#     mag_order = ['Journal', 'BookChapter', 'Conference', 'Repository', 'Book', 'Patent',
#                  'Thesis', 'Dataset', 'no assigned MAG Type']
#
#     figdata.reset_index(inplace=True)
#     figdata['cr_type'] = pd.Categorical(figdata.cr_type, categories=cr_order)
#     figdata['mag_type'] = pd.Categorical(figdata.mag_type, categories=mag_order)
#     figdata.sort_values(['cr_type', 'mag_type'], inplace=True)
#
#     plot = Alluvial(df=figdata,
#                     from_col_name='cr_type',
#                     to_col_name='mag_type',
#                     flow_values_col='num_dois')
#
#     plot.process_data()
#     fig = plot.plotly()
#     fig.write_image('alluvial_all_time.png')
#     af.add_existing_file('alluvial_all_time.png')
#     write_plotly_div(af, fig, 'alluvial_all_time.html')
#
#     figdata = cr_data_with_nulls[cr_data.published_year.isin(CURRENT)].groupby(['cr_type', 'mag_type']).agg(
#         num_dois=pd.NamedAgg(column='num_dois', aggfunc='sum')
#     )
#
#     figdata.reset_index(inplace=True)
#     figdata['cr_type'] = pd.Categorical(figdata.cr_type, categories=cr_order)
#     figdata['mag_type'] = pd.Categorical(figdata.mag_type, categories=mag_order)
#     figdata.sort_values(['cr_type', 'mag_type'], inplace=True)
#
#     plot = Alluvial(df=figdata,
#                     from_col_name='cr_type',
#                     to_col_name='mag_type',
#                     flow_values_col='num_dois')
#
#     plot.process_data()
#     fig = plot.plotly()
#
#     fig.write_image('alluvial_current.png')
#     af.add_existing_file('alluvial_current.png')
#     write_plotly_div(af, fig, 'alluvial_current.html')
#
#

def calculate_overall_coverage(base_df: pd.DataFrame,
                               source_df: pd.DataFrame,
                               source: str,
                               base_comparison: str = 'crossref') -> dict:
    base_total = base_df[f'{base_comparison}_ids'].sum()
    dois_in_source = base_df[f'{source}_ids'].sum()
    source_total = source_df.num_objects.sum()
    source_with_doi = source_df.num_dois.sum()
    source_dois_not_base = source_with_doi - dois_in_source
    total_objects = base_total + (source_total - dois_in_source) + source_dois_not_base
    total_dois = base_total + source_dois_not_base
    objects_wo_dois = total_objects - total_dois

    return dict(
        total_objects=total_objects,
        total_dois=total_dois,
        objects_wo_dois=objects_wo_dois,
        source_no_doi=source_total - source_with_doi,
        source_dois_not_cr=source_dois_not_base,
        cr_in_source=dois_in_source,
        cr_not_in_source=base_total - dois_in_source,
        cr_total=base_total
    )


def overall_comparison(af: AnalyticsFunction,
                       source: str,
                       base_comparison: str = 'crossref'):

    with pd.HDFStore(LOCAL_DATA_PATH) as store:
        base_comparison_data = store[STORE_ELEMENT[base_comparison]]
        source_data = store[STORE_ELEMENT[source]]

    for source in SOURCES:
        if source == base_comparison:
            continue

        with pd.HDFStore(LOCAL_DATA_PATH) as store:
            source_data = store[STORE_ELEMENT[source]]

        for timeframe in TIME_FRAMES.keys():
            filtered_base = base_comparison_data[base_comparison_data.published_year.isin(TIME_FRAMES[timeframe])]
            filtered_source = source_data[source_data.published_year.isin(TIME_FRAMES[timeframe])]

            figdata = calculate_overall_coverage(filtered_base, filtered_source,
                                                 source, base_comparison)
            chart = OverallCoverage(source=FORMATTED_SOURCE_NAMES[source],
                                    data_dict=figdata,
                                    line_offset=0.06)

            fig = chart.plotly()
            filename = f'{source}_{base_comparison}_coverage_{timeframe.lower().replace(" ", "_")}'
            filepath = GRAPH_DIR / filename
            fig.write_image(filepath.with_suffix('.png'))
            af.add_existing_file(filepath.with_suffix('.png'))
            # write_plotly_div(af, fig, 'overall_coverage.html')


def source_in_base_by_pubdate(af,
                              base_comparison: str = 'crossref'):
    with pd.HDFStore(LOCAL_DATA_PATH) as store:
        base_comparison_data = store[STORE_ELEMENT[base_comparison]]

    for source in SOURCES:
        if source == base_comparison:
            continue

        with pd.HDFStore(LOCAL_DATA_PATH) as store:
            source_data = store[STORE_ELEMENT[source]]

        year_range = SOURCE_IN_BASE_YEAR_RANGE

        figdata = pd.DataFrame(index=year_range,
                               data=[calculate_overall_coverage(
                                   base_df=base_comparison_data[base_comparison_data.published_year == year],
                                   source_df=source_data[source_data.published_year == year],
                                   source=source
                               )
                                   for year in year_range])

        figdata['pc_source_in_base'] = figdata.cr_in_source / figdata.cr_total * 100

        chart = BarLine(xdata=figdata.index,
                        bardata=figdata.cr_total,
                        barname=f'Registered {FORMATTED_SOURCE_NAMES[base_comparison]} DOIs',
                        linedata=figdata.pc_source_in_base,
                        linename=f'Crossref DOIs in {FORMATTED_SOURCE_NAMES[source]} (%)')

        fig = chart.plotly()
        filename = f'{base_comparison}_in_{source}_by_pubdate'
        filepath = GRAPH_DIR / filename
        fig.write_image(filepath.with_suffix('.png'))
        af.add_existing_file(filepath.with_suffix('.png'))
        # write_plotly_div(af, fig, 'cr_in_mag_barline.html')

