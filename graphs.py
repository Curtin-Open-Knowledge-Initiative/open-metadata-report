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
from parameters import *
from report_graphs import ValueAddBar, ValueAddByCrossrefType, OverallCoverage, BarLine, Alluvial

def load_cache_data(af: AnalyticsFunction,
                    function_name: Union[str, Callable],
                    element: str,
                    filename: Optional[str] = None):
    """Convenience function for loading preprepared DataFrames from the cache
    :param filename:
    :param function_name:
    :param element: Component of the filecache to load
    :param af
    Downloaded query data is collected as DataFrames and stored in and HDFS store as DataFrames. This
    is a convenient function for reloading data from that frame.
    """

    if callable(function_name):
        afunction_name = function_name.__name__
    else:
        afunction_name = function_name

    store_filepath = af.path_to_cached_file(
        filename, afunction_name)

    with pd.HDFStore(store_filepath) as store:
        if f"/{element}" not in store.keys():
            return None
        df = store[element]

    return df


def value_add_graphs(af: AnalyticsFunction):

    with pd.read_hdf(LOCAL_DATA_PATH) as store:
        cr_data = store[STORE_ELEMENT['crossref']]

    sum_all = cr_data.sum(axis=0)
    sum_2020 = cr_data[cr_data.published_year == 2020].sum(axis=0)
    sum_current = cr_data[cr_data.published_year.isin(CURRENT)].sum(axis=0)

    # TODO - Column matching here
    cols = ['dois_with_cr_affiliation_strings',
            'dois_with_cr_orcid',
            'dois_with_cr_abstract',
            'dois_with_cr_subjects',
            'dois_with_cr_citations',
            'dois_with_cr_references',
            'dois_with_cr_open_references',
            'dois_mag_aff_string_but_not_cr',
            'dois_with_mag_author_id_but_not_cr_orcid',
            'dois_with_mag_not_cr_abstract',
            'dois_with_mag_field0',
            'dois_with_mag_field_not_cr_subject',
            'dois_with_mag_not_cr_citations',
            'dois_more_mag_citations',
            'dois_with_mag_not_cr_references',
            'dois_more_mag_references',
            'dois_with_mag_not_cr_open_references'
            ]

    summary_table = collate_value_add_values(sum_all, cols)
    summary_table = summary_table.append(collate_value_add_values(sum_current, cols))
    summary_table = summary_table.append(collate_value_add_values(sum_2020, cols))

    summary_table['Time Period'] = ['All Time',
                                    'Crossref Current 2019-21',
                                    '2020 Only']

    for time_period in ['All Time',
                        'Crossref Current 2019-21',
                        '2020 Only']:
        chart = ValueAddBar(df=summary_table[summary_table['Time Period'] == time_period],
                            categories=['Crossref', 'MAG added value'],
                            xs=['Affiliations', 'Abstracts', 'Citations to', 'References from'])
        fig = chart.plotly()
        filename = f'value_add_{time_period.lower().replace(" ", "_")}.'
        fig.write_image(GRAPH_DIR / filename + 'png')
        af.add_existing_file(GRAPH_DIR / filename + 'png')
        # write_plotly_div(af, fig, filename + 'html')

        chart = ValueAddBar(df=summary_table[summary_table['Time Period'] == time_period],
                            categories=['Crossref', 'MAG added value'],
                            xs=['Subjects'],
                            stackedbar=False)
        fig = chart.plotly()
        filename = f'value_add_subject_{time_period.lower().replace(" ", "_")}.'
        fig.write_image(GRAPH_DIR / filename + 'png')
        af.add_existing_file(GRAPH_DIR / filename + 'png')
        # write_plotly_div(af, fig, filename + 'html')


def collate_value_add_values(df: pd.DataFrame,
                             cols: list):
    """
    Convenience function for cleaning up the value add tables
    :param df: summed data frame from the doi_table_categories_query
    :param cols: type: list set of columns to calculate percentages for
    :return df: type: pd.DataFrame modified dataframe with percentages calculated and all columns remaining
    """

    if type(df) == pd.Series:
        df = pd.DataFrame(df).transpose()

    for col in cols:
        df[f'pc_{col}'] = np.round(df[col] / df['num_dois'] * 100, 1)

    return df


def alluvial_graph(af: AnalyticsFunction):
    cr_data = load_cache_data(af,
                              function_name=get_doi_table_data,
                              element='doi_categories',
                              filename=CR_DATA_FILENAME)
    cr_data_with_nulls = cr_data.replace(to_replace={'cr_type': {
        None: 'no assigned Crossref Type'
    },
        'mag_type': {
            None: 'no assigned MAG Type'
        }
    }
    )

    figdata = cr_data_with_nulls.groupby(['cr_type', 'mag_type']).agg(
        num_dois=pd.NamedAgg(column='num_dois', aggfunc='sum')
    )

    cr_order = ['journal-article', 'book-chapter', 'proceedings-article', 'dataset',
                'book', 'journal-issue', 'reference-entry', 'posted-content', 'report',
                'monograph', 'component', 'proceedings', 'report-series', 'book-section',
                'book-part', 'standard', 'book-track', 'other', 'no assigned Crossref Type']
    mag_order = ['Journal', 'BookChapter', 'Conference', 'Repository', 'Book', 'Patent',
                 'Thesis', 'Dataset', 'no assigned MAG Type']

    figdata.reset_index(inplace=True)
    figdata['cr_type'] = pd.Categorical(figdata.cr_type, categories=cr_order)
    figdata['mag_type'] = pd.Categorical(figdata.mag_type, categories=mag_order)
    figdata.sort_values(['cr_type', 'mag_type'], inplace=True)

    plot = Alluvial(df=figdata,
                    from_col_name='cr_type',
                    to_col_name='mag_type',
                    flow_values_col='num_dois')

    plot.process_data()
    fig = plot.plotly()
    fig.write_image('alluvial_all_time.png')
    af.add_existing_file('alluvial_all_time.png')
    write_plotly_div(af, fig, 'alluvial_all_time.html')

    figdata = cr_data_with_nulls[cr_data.published_year.isin(CURRENT)].groupby(['cr_type', 'mag_type']).agg(
        num_dois=pd.NamedAgg(column='num_dois', aggfunc='sum')
    )

    figdata.reset_index(inplace=True)
    figdata['cr_type'] = pd.Categorical(figdata.cr_type, categories=cr_order)
    figdata['mag_type'] = pd.Categorical(figdata.mag_type, categories=mag_order)
    figdata.sort_values(['cr_type', 'mag_type'], inplace=True)

    plot = Alluvial(df=figdata,
                    from_col_name='cr_type',
                    to_col_name='mag_type',
                    flow_values_col='num_dois')

    plot.process_data()
    fig = plot.plotly()

    fig.write_image('alluvial_current.png')
    af.add_existing_file('alluvial_current.png')
    write_plotly_div(af, fig, 'alluvial_current.html')


def calculate_overall_coverage(mag_data: pd.DataFrame,
                               cr_data: pd.DataFrame) -> dict:
    cr_total = cr_data.num_dois.sum()
    cr_in_mag = cr_data.dois_with_mag_id.sum()
    mag_total = mag_data.num_objects.sum()
    mag_with_doi = mag_data.num_dois.sum()
    mag_dois_not_cr = mag_with_doi - cr_in_mag
    total_objects = cr_total + (mag_total - mag_with_doi) + mag_dois_not_cr
    total_dois = cr_total + mag_dois_not_cr
    objects_wo_dois = total_objects - total_dois

    return dict(
        total_objects=total_objects,
        total_dois=total_dois,
        objects_wo_dois=objects_wo_dois,
        mag_no_doi=mag_total - mag_with_doi,
        mag_dois_not_cr=mag_dois_not_cr,
        cr_in_mag=cr_in_mag,
        cr_not_in_mag=cr_total - cr_in_mag,
        cr_total=cr_total
    )


def overall_comparison(af: AnalyticsFunction):
    cr_data = load_cache_data(af,
                              function_name=get_doi_table_data,
                              element='doi_categories',
                              filename=CR_DATA_FILENAME)

    cr_sum_all = cr_data.sum(axis=0)
    cr_sum_2020 = cr_data[cr_data.published_year == 2020].sum(axis=0)
    cr_sum_current = cr_data[cr_data.published_year.isin(CURRENT)].sum(axis=0)

    mag_data = load_cache_data(af,
                               function_name=get_mag_table_data,
                               element='mag_categories',
                               filename=MAG_DATA_FILENAME)

    mag_sum_all = mag_data.sum(axis=0)
    mag_sum_2020 = mag_data[mag_data.Year == 2020].sum(axis=0)
    mag_sum_current = mag_data[mag_data.Year.isin(CURRENT)].sum(axis=0)

    figdata_all = calculate_overall_coverage(mag_sum_all, cr_sum_all)
    chart = OverallCoverage(figdata_all,
                            line_offset=0.06)
    # line_offset=0.08)
    fig = chart.plotly()
    fig.write_image('overall_coverage.png')
    af.add_existing_file('overall_coverage.png')
    write_plotly_div(af, fig, 'overall_coverage.html')

    figdata_2020 = calculate_overall_coverage(mag_sum_2020, cr_sum_2020)
    chart = OverallCoverage(figdata_2020,
                            line_offset=0.06)
    # line_offset=0.08)
    fig = chart.plotly()
    fig.write_image('2020_coverage.png')
    af.add_existing_file('2020_coverage.png')

    figdata_current = calculate_overall_coverage(mag_sum_current, cr_sum_current)
    chart = OverallCoverage(figdata_current,
                            line_offset=0.06)
    # line_offset=0.08)
    fig = chart.plotly()
    fig.write_image('current_coverage.png')
    af.add_existing_file('current_coverage.png')
    write_plotly_div(af, fig, 'current_coverage.html')


def mag_in_crossref_by_pubdate(af):
    cr_data = load_cache_data(af,
                              function_name=get_doi_table_data,
                              element='doi_categories',
                              filename=CR_DATA_FILENAME)

    mag_data = load_cache_data(af,
                               function_name=get_mag_table_data,
                               element='mag_categories',
                               filename=MAG_DATA_FILENAME)

    year_range = range(1980, 2022)

    figdata = pd.DataFrame(index=year_range,
                           data=[calculate_overall_coverage(
                               mag_data=mag_data[mag_data.Year == year],
                               cr_data=cr_data[cr_data.published_year == year])
                               for year in year_range])

    figdata['pc_mag_in_cr'] = figdata.cr_in_mag / figdata.cr_total * 100

    chart = BarLine(xdata=figdata.index,
                    bardata=figdata.cr_total,
                    linedata=figdata.pc_mag_in_cr)

    fig = chart.plotly()

    fig.write_image('cr_in_mag_barline.png')
    af.add_existing_file('cr_in_mag_barline.png')
    write_plotly_div(af, fig, 'cr_in_mag_barline.html')