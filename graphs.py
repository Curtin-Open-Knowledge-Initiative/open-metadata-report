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
import copy
import plotly.graph_objects as go
from typing import Optional, Callable, Union
from precipy.analytics_function import AnalyticsFunction

from observatory.reports import report_utils
from data_parameters import *
from graph_parameters import *
from report_graphs import (
    ValueAddBar,
    ValueAddByCrossrefType,
    ValueAddByCrossrefTypeHorizontal,
    OverallCoverage,
    BarLine,
    Alluvial
)


def value_add_graphs(af: AnalyticsFunction,
                     base_comparison: str = 'crossref'):
    """
    Generate graphs that provide information on the value add of a source compared to base_comparison

    :param af: AnalyticsFunction for the precipy run
    :param source: Lowercase string name of the source being compared
    :param base_comparison: Lowercase string name of the base_comparison, crossref is the default
    """

    print('Generating value add graphs...')
    with pd.HDFStore(LOCAL_DATA_PATH) as store:
        base_comparison_data = store[STORE_ELEMENT[base_comparison]]

    for source in SOURCES:
        if source == base_comparison:
            continue

        for timeframe in TIME_FRAMES.keys():
            filtered = base_comparison_data[base_comparison_data.published_year.isin(TIME_FRAMES[timeframe])]
            filtered_sum = filtered.sum(axis=0)
            figdata = collate_value_add_values(filtered_sum, ALL_COLLATED_COLUMNS)

            # Stacked Bar
            chart = ValueAddBar(df=figdata,
                                categories=[FORMATTED_SOURCE_NAMES[base_comparison],
                                            f'{FORMATTED_SOURCE_NAMES[source]} Added Value'],
                                xs=STACKED_BAR_SUMMARY_XS,
                                ys=VALUE_ADD_META[base_comparison][source]['ys'])

            fig = chart.plotly()
            filename = f'value_add_stacked_{source}_{timeframe.lower().replace(" ", "_")}'
            filepath = GRAPH_DIR / filename
            fig.write_image(filepath.with_suffix('.png'))
            af.add_existing_file(filepath.with_suffix('.png'))

            # Side by side bar (including Fields)
            # Stacked Bar
            chart = ValueAddBar(df=figdata,
                                categories=[FORMATTED_SOURCE_NAMES[base_comparison],
                                            f'{FORMATTED_SOURCE_NAMES[source]}'],
                                xs=SIDEBYSIDE_BAR_SUMMARY_XS,
                                ys=VALUE_ADD_META[base_comparison][source]['ys'],
                                stackedbar=False)

            fig = chart.plotly()
            filename = f'value_add_sidebyside_{source}_{timeframe.lower().replace(" ", "_")}'
            filepath = GRAPH_DIR / filename
            fig.write_image(filepath.with_suffix('.png'))
            af.add_existing_file(filepath.with_suffix('.png'))

            # Details graph for each metadata element
            for metadata_element in VALUE_ADD_META[base_comparison][source]['xs']:
                sum_by_type = filtered.groupby('type').sum().reset_index()
                collated_sum_by_type = collate_value_add_values(sum_by_type, ALL_COLLATED_COLUMNS)

                chart = ValueAddByCrossrefType(df=collated_sum_by_type,
                                               metadata_element=metadata_element,
                                               ys=VALUE_ADD_META[base_comparison][source]['ys'],
                                               categories=[
                                                   FORMATTED_SOURCE_NAMES[base_comparison],
                                                   f'{FORMATTED_SOURCE_NAMES[source]}'],
                                               stackedbar=False
                                               )
                fig = chart.plotly()

                filename = f'value_add_{source}_{timeframe.lower().replace(" ", "_")}_for_{metadata_element.replace(" ", "_").lower()}_by_cr_type'
                filepath = GRAPH_DIR / filename
                fig.write_image(filepath.with_suffix('.png'))
                af.add_existing_file(filepath.with_suffix('.png'))


def source_coverage_by_crossref_type(af: AnalyticsFunction,
                                     base_comparison: str = 'crossref'):
    """
    Graph the coverage of the source compared to the base comparison by crossref-type
    """

    with pd.HDFStore(LOCAL_DATA_PATH) as store:
        base_comparison_data = store[STORE_ELEMENT[base_comparison]]

    for source in SOURCES:
        if source == base_comparison:
            continue

        figdata = base_comparison_data.groupby('type').agg(
            crossref_dois=pd.NamedAgg(column=f'{base_comparison}_dois', aggfunc='sum'),
            in_source=pd.NamedAgg(column=f'{source}_ids', aggfunc='sum'),
            source_has_type=pd.NamedAgg(column=f'{source}_has_{source}_type', aggfunc='sum')
        )

        figdata['source_without_type'] = figdata.in_source - figdata.source_has_type
        figdata['not_in_source'] = figdata.crossref_dois - figdata.in_source
        figdata = collate_value_add_values(figdata, ['source_has_type',
                                                     'source_without_type',
                                                     'not_in_source'])
        figdata.reset_index(inplace=True)

        chart = ValueAddByCrossrefTypeHorizontal(df=figdata,
                                                 categories=[f'in {FORMATTED_SOURCE_NAMES[source]} with Document Type',
                                                             f'in {FORMATTED_SOURCE_NAMES[source]} without Document Type',
                                                             f'Not in {FORMATTED_SOURCE_NAMES[source]}'],
                                                 metadata_element='dummy',
                                                 ys={
                                                     f'in {FORMATTED_SOURCE_NAMES[source]} with Document Type': {
                                                         'dummy': 'pc_source_has_type'},
                                                     f'in {FORMATTED_SOURCE_NAMES[source]} without Document Type': {
                                                         'dummy': 'pc_source_without_type'},
                                                     f'Not in {FORMATTED_SOURCE_NAMES[source]}': {
                                                         'dummy': 'pc_not_in_source'}
                                                 }
                                                 )

        # Modify the bar colors here
        fig = chart.plotly(palette=['#F6671E', '#FAA77C', '#CCCCCC'])
        filename = f'{source}_coverage_by_crossref_type'
        filepath = GRAPH_DIR / filename
        fig.write_image(filepath.with_suffix('.png'))
        af.add_existing_file(filepath.with_suffix('.png'))
        # write_plotly_div(af, fig, 'mag_coverage_by_crossref_type.html')


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

    column_names = []
    columns_data = []
    for col in cols:
        if col in df.columns:
            column_names.append(f'pc_{col}')
            columns_data.append(np.round(df[col] / df['crossref_dois'] * 100, 1))

    added_columns = pd.DataFrame({name: data for name, data in zip(column_names, columns_data)})
    df = pd.concat([df, added_columns], axis=1)
    return df


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
                       base_comparison: str = 'crossref'):
    with pd.HDFStore(LOCAL_DATA_PATH) as store:
        base_comparison_data = store[STORE_ELEMENT[base_comparison]]

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

