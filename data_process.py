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
import requests
import jinja2

import pandas as pd
import numpy as np
from google.cloud import bigquery
from git import Repo

from observatory.reports import report_utils
from precipy.analytics_function import AnalyticsFunction
from report_data_processing.sql import load_sql_to_string
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
from observatory.reports.report_utils import generate_table_data




def openalex_to_truthtable(af: AnalyticsFunction,
                                  source: str = 'openalex',
                                  rerun: bool = RERUN,
                                  verbose: bool = VERBOSE):
#    pass

    """
    Convert OpenAlex Format Works Table to Truthtable

    Note that OpenAlex uses the fully qualified URL form of the doi in lower case and needs conversion.
    See the query for details.
    """

    query = load_sql_to_string('openalex_truthtable.sql',
                               parameters=dict(table=TABLES[source]),
                               directory=SQL_DIRECTORY)

    if not report_utils.bigquery_rerun(af, rerun, verbose, source):
        print(f"""Query is:
+
    {query}

    """)
        print(f'Destination Table: {SOURCE_TRUTH_TABLES[source]}')
        return

    with bigquery.Client() as client:
        job_config = bigquery.QueryJobConfig(destination=SOURCE_TRUTH_TABLES[source],
                                             create_disposition='CREATE_IF_NEEDED',
                                             write_disposition=WRITE_DISPOSITION)

        query_job = client.query(query, job_config=job_config)  # Make an API request.
        query_job.result()  # Wait for the job to complete.

    if verbose:
        print('...completed')


def crossref_to_truthtable(af: AnalyticsFunction,
                           source: str = 'crossref',
                           rerun: bool = RERUN,
                           verbose: bool = VERBOSE):
    """
    Calculate truthtable for Crossref
    """

    query = load_sql_to_string('crossref_truthtable_query.sql',
                               parameters=dict(table=TABLES[source]),
                               directory=SQL_DIRECTORY)

    if not report_utils.bigquery_rerun(af, rerun, verbose):
        print(f"""Query is:

{query}

""")
        print(f'Destination Table: {SOURCE_TRUTH_TABLES[source]}')
        return

    with bigquery.Client() as client:
        job_config = bigquery.QueryJobConfig(destination=SOURCE_TRUTH_TABLES[source],
                                             create_disposition='CREATE_IF_NEEDED',
                                             write_disposition=WRITE_DISPOSITION)

        query_job = client.query(query, job_config=job_config)  # Make an API request.
        query_job.result()  # Wait for the job to complete.

    if verbose:
        print('...completed')


def source_category_query(af: AnalyticsFunction,
                          rerun: bool = RERUN,
                          verbose: bool = VERBOSE):
    """
    Query and download category data from the intermediate tables
    """

    for source in NON_BASE_SOURCES:
        query_template = load_sql_to_string('source_categories_query.sql.jinja2',
                                            directory=SQL_DIRECTORY)

        data_items = list(set(CATEGORY_DATA_ITEMS + SOURCE_DATA_ITEMS[source]))
        data_items.sort()
        data = dict(
            table=SOURCE_TRUTH_TABLES[source],
            data_items=data_items
        )
        query = jinja2.Template(query_template).render(data)

        if not report_utils.bigquery_rerun(af, rerun, verbose, source):
            print(f"""Query is:
            
    {query}
    
    """)
            continue

        categories = pd.read_gbq(query=query,
                                 project_id=PROJECT_ID)

#        with pd.HDFStore(LOCAL_DATA_PATH) as store:
#        store[STORE_ELEMENT[source]] = categories

        categories.to_csv(CSV_FILE[source])
        af.add_existing_file(CSV_FILE[source])

        if verbose:
            print('...completed')


def dois_category_query(af: AnalyticsFunction,
                        rerun: bool = RERUN,
                        verbose: bool = VERBOSE):
    """
    Query and download category data from the quasi doi table
    """

    query_template = load_sql_to_string('comparison_categories_query.sql.jinja2',
                                        directory=SQL_DIRECTORY)

    data = dict(
        sources={source: SOURCE_TRUTH_TABLES[source] for source in SOURCES},
        data_items=SOURCE_DATA_ELEMENTS
    )
    query = jinja2.Template(query_template).render(data)

    if not report_utils.bigquery_rerun(af, rerun, verbose):
        print(f"""Query is:      
{query}

""")
        return

    # Run the query and download data
    categories = pd.read_gbq(query=query,
                             project_id=PROJECT_ID)

#    with pd.HDFStore(LOCAL_DATA_PATH) as store:
#        store[STORE_ELEMENT['crossref']] = categories

    categories.to_csv(CSV_FILE['crossref'])
    af.add_existing_file(CSV_FILE['crossref'])

    if verbose:
        print('...completed')


def save_data_parameters(af):
    """
    Write out JSON for the data parameters
    """

    import data_parameters as params
    for f in af.generate_file('data_parameters.json'):
        json.dump({item: getattr(params, item) for item in dir(params) if not item.startswith('__')},
                  f,
                  default=str)

    import graph_parameters as params
    for f in af.generate_file('graph_parameters.json'):
        json.dump({item: getattr(params, item) for item in dir(params) if not item.startswith('__')},
                  f,
                  default=str)

#   for source in SOURCES:
#        with pd.HDFStore(LOCAL_DATA_PATH) as store:
#            categories = store[STORE_ELEMENT[source]]

#        categories.to_csv(CSV_FILE[source])
#        af.add_existing_file(CSV_FILE[source])


def git_status(af):
    """
    Record Git Status for Current State of the Repo
    """

    repo = Repo(search_parent_directories=True)
    print('This report was run from the git commit hash: ' + repo.head.object.hexsha)
    changedfiles = [item.a_path for item in repo.index.diff(None)]
    if len(changedfiles) > 0:
        print('WARNING: This report was run with local changes that were not committed to the following files: ')
        print(changedfiles)

    for f in af.generate_file('git_status.json'):
        json.dump(dict(
            sha=repo.head.object.hexsha,
            changedfiles=[item.a_path for item in repo.index.diff(None)],
            branch=repo.active_branch.name),
            f
        )


## Graphs

def value_add_graphs(af: AnalyticsFunction,
                     base_comparison: str = BASE_COMPARISON):
    """
    Generate graphs that provide information on the value add of a source compared to base_comparison

    :param af: AnalyticsFunction for the precipy run
    :param source: Lowercase string name of the source being compared
    :param base_comparison: Lowercase string name of the base_comparison, crossref is generally the default which is
    set as BASE_COMPARISON in data_parameters.py
    """

    print('Generating value add graphs...')
#    with pd.HDFStore(LOCAL_DATA_PATH) as store:
#        base_comparison_data = store[STORE_ELEMENT[base_comparison]]

    base_comparison_data = pd.read_csv(CSV_FILE[base_comparison])

    for source in NON_BASE_SOURCES:

        for timeframe in TIME_FRAMES.keys():
            filtered = base_comparison_data[base_comparison_data.published_year.isin(TIME_FRAMES[timeframe])]
            filtered_sum = filtered.sum(axis=0)
            figdata = collate_value_add_values(filtered_sum,
                                               ALL_COLLATED_COLUMNS,
                                               'crossref_dois')

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
                collated_sum_by_type = collate_value_add_values(sum_by_type,
                                                                ALL_COLLATED_COLUMNS,
                                                                'crossref_dois')

                # Stacked Bar
                chart = ValueAddByCrossrefType(df=collated_sum_by_type,
                                               metadata_element=metadata_element,
                                               ys=VALUE_ADD_META[base_comparison][source]['ys'],
                                               categories=[
                                                   FORMATTED_SOURCE_NAMES[base_comparison],
                                                   f'{FORMATTED_SOURCE_NAMES[source]} Added Value']
                                               )

                chart.process_data(
                    doc_types=CROSSREF_TYPES,
                )

                fig = chart.plotly()
                filename = f'value_add_stacked_{source}_{timeframe.lower().replace(" ", "_")}_for_{metadata_element.replace(" ", "_").lower()}_by_cr_type'
                filepath = GRAPH_DIR / filename
                fig.write_image(filepath.with_suffix('.png'))
                af.add_existing_file(filepath.with_suffix('.png'))

                # Side by side bar
                chart = ValueAddByCrossrefType(df=collated_sum_by_type,
                                               metadata_element=metadata_element,
                                               ys=VALUE_ADD_META[base_comparison][source]['ys'],
                                               categories=[
                                                   FORMATTED_SOURCE_NAMES[base_comparison],
                                                   f'{FORMATTED_SOURCE_NAMES[source]}'],
                                               stackedbar=False
                                               )
                fig = chart.plotly()
                filename = f'value_add_sidebyside_{source}_{timeframe.lower().replace(" ", "_")}_for_{metadata_element.replace(" ", "_").lower()}_by_cr_type'
                filepath = GRAPH_DIR / filename
                fig.write_image(filepath.with_suffix('.png'))
                af.add_existing_file(filepath.with_suffix('.png'))

def source_coverage_by_crossref_type(af: AnalyticsFunction,
                                     base_comparison: str = BASE_COMPARISON):
    """
    Graph the coverage of the source compared to the base comparison by crossref-type
    """

#    with pd.HDFStore(LOCAL_DATA_PATH) as store:
#        base_comparison_data = store[STORE_ELEMENT[base_comparison]]

    base_comparison_data = pd.read_csv(CSV_FILE[base_comparison])

    for source in NON_BASE_SOURCES:

        # TODO Cleanup variable names here to abstract away from crossref to generalised base comparison
        figdata = base_comparison_data.groupby('type').agg(
            in_base_comparison=pd.NamedAgg(column=f'{base_comparison}_dois', aggfunc='sum'),
            in_source=pd.NamedAgg(column=f'{source}_ids', aggfunc='sum'),
            source_has_type=pd.NamedAgg(column=f'{source}_has_{source}_type', aggfunc='sum')
        )

        figdata['source_without_type'] = figdata.in_source - figdata.source_has_type
        figdata['not_in_source'] = figdata.in_base_comparison - figdata.in_source
        figdata = collate_value_add_values(figdata,
                                           ['source_has_type',
                                            'source_without_type',
                                            'not_in_source'],
                                           'in_base_comparison')
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

        chart.process_data(
            doc_types=CROSSREF_TYPES,
            palette=['#FF7F0E', '#FAA77C', '#C0C0C0']
        )
        fig = chart.plotly()

        # TODO Cleanup file name here (and downstream!) to abstract away from crossref to generalised base comparison
        filename = f'{source}_coverage_by_crossref_type'
        filepath = GRAPH_DIR / filename
        fig.write_image(filepath.with_suffix('.png'))
        af.add_existing_file(filepath.with_suffix('.png'))
        # write_plotly_div(af, fig, f'{source}_coverage_by_crossref_type.html')


def collate_value_add_values(df: pd.DataFrame,
                             cols: list,
                             total_column: str):
    """
    Convenience function for cleaning up the value add tables
    :param df: summed data frame from the doi_table_categories_query
    :param cols: type: list set of columns to calculate percentages for
    :param total_column: type: str Name of column that contains totals for calculation of percentages

    :return df: type: pd.DataFrame modified dataframe with percentages calculated and all columns remaining
    """

    if type(df) == pd.Series:
        df = pd.DataFrame(df).transpose()

    column_names = []
    columns_data = []
    for col in cols:
        if col in df.columns:
            column_names.append(f'pc_{col}')
            columns_data.append(np.round(df[col] / df[total_column] * 100, 1))

    added_columns = pd.DataFrame({name: data for name, data in zip(column_names, columns_data)})
    df = pd.concat([df, added_columns], axis=1)
    return df

def calculate_overall_coverage(base_df: pd.DataFrame,
                               source_df: pd.DataFrame,
                               source: str,
                               base_comparison: str = BASE_COMPARISON) -> dict:
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
        cr_total=base_total,
        #Added for dois_in_source_by_pubdate
        source_total=source_total,
        source_dois=source_with_doi
    )


def overall_comparison(af: AnalyticsFunction,
                       base_comparison: str = BASE_COMPARISON):
#    with pd.HDFStore(LOCAL_DATA_PATH) as store:
#        base_comparison_data = store[STORE_ELEMENT[base_comparison]]

    base_comparison_data = pd.read_csv(CSV_FILE[base_comparison])

    for source in SOURCES:
        if source == base_comparison:
            continue

#        with pd.HDFStore(LOCAL_DATA_PATH) as store:
#            source_data = store[STORE_ELEMENT[source]]

        source_data = pd.read_csv(CSV_FILE[source])

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
                              base_comparison: str = BASE_COMPARISON):
#    with pd.HDFStore(LOCAL_DATA_PATH) as store:
#        base_comparison_data = store[STORE_ELEMENT[base_comparison]]

    base_comparison_data = pd.read_csv(CSV_FILE[base_comparison])

    for source in SOURCES:
        if source == base_comparison:
            continue

#        with pd.HDFStore(LOCAL_DATA_PATH) as store:
#            source_data = store[STORE_ELEMENT[source]]

        source_data = pd.read_csv(CSV_FILE[source])

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


## Graphs for comparing source database with itself (eg dois vs non-dois)

def value_add_self_graphs(af: AnalyticsFunction,
                          # base_comparison: str = BASE_COMPARISON):
                          base_comparison: str = NON_BASE_SOURCES[0]):
#    pass

    """
    Generate graphs that provide information on metadata coverage of dois and non-dois in a given source
    Adaptation of value_add_graphs

    :param af: AnalyticsFunction for the precipy run
    :param source: Lowercase string name of the source being compared
    :param base_comparison: Lowercase string name of the base_comparison, set the same as the source being compared
    use NON_BASE_SOURCES in data_parameters.py
    """
    # TODO Dynamically set base_comparison when looping over multiple sources?

    print('Generating value add graphs...')
#    with pd.HDFStore(LOCAL_DATA_PATH) as store:
#        base_comparison_data = store[STORE_ELEMENT[base_comparison]]

    base_comparison_data = pd.read_csv(CSV_FILE[base_comparison])

    for source in NON_BASE_SOURCES:



        # Replace None (which is not a string) values with string 'none' to include in aggregation
        # base_comparison_data[['type']] = base_comparison_data[['type']].fillna(value='none')

        for timeframe in TIME_FRAMES.keys():
            filtered = base_comparison_data[base_comparison_data.published_year.isin(TIME_FRAMES[timeframe])]
            filtered_sum = filtered.sum(axis=0)
            figdata = collate_value_add_self_values(filtered_sum,
                                               PRESENCE_COLUMNS_SELF)

            # Side by side bar (including Fields)
            chart = ValueAddBar(df=figdata,
                                categories=[f'{FORMATTED_SOURCE_NAMES[source]} DOIs',
                                            f'{FORMATTED_SOURCE_NAMES[source]} non-DOIs'],
                                xs=SIDEBYSIDE_BAR_SUMMARY_XS,
                                ys=VALUE_ADD_META[base_comparison][source]['ys'],
                                stackedbar=False)

            # Modify chart parameters here
            chart.process_data(
                palette=['#FF7F0E', '#C0C0C0']
            )

            fig = chart.plotly()
            filename = f'value_add_self_sidebyside_{source}_{timeframe.lower().replace(" ", "_")}'
            filepath = GRAPH_DIR / filename
            fig.write_image(filepath.with_suffix('.png'))
            af.add_existing_file(filepath.with_suffix('.png'))

           #Detailed graphs per metadata element

            for metadata_element in VALUE_ADD_META[base_comparison][source]['xs']:
                sum_by_type = filtered.groupby('type').sum().reset_index()
                collated_sum_by_type = collate_value_add_self_values(sum_by_type,
                                                                PRESENCE_COLUMNS_SELF)

                # Side by side bar
                chart = ValueAddByCrossrefType(df=collated_sum_by_type,
                                                  metadata_element=metadata_element,
                                               ys=VALUE_ADD_META[base_comparison][source]['ys'],
                                               categories=[f'{FORMATTED_SOURCE_NAMES[source]} DOIs',
                                                           f'{FORMATTED_SOURCE_NAMES[source]} non-DOIs'],
                                               stackedbar=False
                                               )

                #Modify chart parameters here
                chart.process_data(
                    doc_types=CROSSREF_TYPES,
                    palette=['#FF7F0E', '#C0C0C0']
                )

                fig = chart.plotly()
                filename = f'value_add_self_sidebyside_{source}_{timeframe.lower().replace(" ", "_")}_for_{metadata_element.replace(" ", "_").lower()}_by_type'
                filepath = GRAPH_DIR / filename
                fig.write_image(filepath.with_suffix('.png'))
                af.add_existing_file(filepath.with_suffix('.png'))


def source_coverage_self_by_type(af: AnalyticsFunction,
                                 # base_comparison: str = BASE_COMPARISON):
                                 base_comparison: str = NON_BASE_SOURCES[0]):
    """
    Graph the coverage of dois and non-dois in source by source type
    Adapted from source_coverage_by_crossref_type
    """
    # TODO Dynamically set base_comparison when looping over multiple sources?

#    with pd.HDFStore(LOCAL_DATA_PATH) as store:
#        base_comparison_data = store[STORE_ELEMENT[base_comparison]]

    base_comparison_data = pd.read_csv(CSV_FILE[base_comparison])

    for source in NON_BASE_SOURCES:

        #Replace None (which is not a string) values with string 'none' to include in aggregation
        figdata = base_comparison_data
        figdata[['type']] = base_comparison_data[['type']].fillna(value='none')

        figdata = base_comparison_data.groupby('type').agg(
            source_objects=pd.NamedAgg(column='num_objects', aggfunc='sum'),
            source_dois=pd.NamedAgg(column='num_dois', aggfunc='sum'),
            source_non_dois=pd.NamedAgg(column='num_non_dois', aggfunc='sum')
        )

        figdata = collate_value_add_values(figdata,
                                           ['source_dois', 'source_non_dois'],
                                           'source_objects')
        figdata.reset_index(inplace=True)


        chart = ValueAddByCrossrefTypeHorizontal(df=figdata,
                                       categories=[f'{FORMATTED_SOURCE_NAMES[source]} DOIs',
                                                   f'{FORMATTED_SOURCE_NAMES[source]} non-DOIs'],
                                       metadata_element='dummy',
                                       ys={
                                           f'{FORMATTED_SOURCE_NAMES[source]} DOIs': {
                                               'dummy': 'pc_source_dois'},
                                           f'{FORMATTED_SOURCE_NAMES[source]} non-DOIs': {
                                               'dummy': 'pc_source_non_dois'}
                                       }
                                       )
        # Modify chart parameters here
        chart.process_data(
            doc_types = OPENALEX_TYPES,
            palette = ['#FF7F0E', '#C0C0C0']
        )
        fig = chart.plotly()
        filename = f'{source}_coverage_self_by_type'
        filepath = GRAPH_DIR / filename
        fig.write_image(filepath.with_suffix('.png'))
        af.add_existing_file(filepath.with_suffix('.png'))


def dois_in_source_by_pubdate(af,
                              base_comparison: str = BASE_COMPARISON):
    """
       Graph the coverage of dois in source by year of publication
       Adapted from source_in_base_by_pubdate
       """

#    with pd.HDFStore(LOCAL_DATA_PATH) as store:
#        base_comparison_data = store[STORE_ELEMENT[base_comparison]]

    base_comparison_data = pd.read_csv(CSV_FILE[base_comparison])

    for source in SOURCES:
        if source == base_comparison:
            continue

#        with pd.HDFStore(LOCAL_DATA_PATH) as store:
#            source_data = store[STORE_ELEMENT[source]]

        source_data = pd.read_csv(CSV_FILE[source])

        year_range = SOURCE_IN_BASE_YEAR_RANGE

        figdata = pd.DataFrame(index=year_range,
                               data=[calculate_overall_coverage(
                                   base_df=base_comparison_data[base_comparison_data.published_year == year],
                                   source_df=source_data[source_data.published_year == year],
                                   source=source
                               )
                                   for year in year_range])

        figdata['pc_dois_in_source'] = figdata.source_dois / figdata.source_total * 100

        chart = BarLine(xdata=figdata.index,
                        bardata=figdata.source_total,
                        barname=f'All {FORMATTED_SOURCE_NAMES[source]} records',
                        linedata=figdata.pc_dois_in_source,
                        linename=f'{FORMATTED_SOURCE_NAMES[source]} with DOIs (%)')

        fig = chart.plotly()
        filename = f'dois_in_{source}_by_pubdate'
        filepath = GRAPH_DIR / filename
        fig.write_image(filepath.with_suffix('.png'))
        af.add_existing_file(filepath.with_suffix('.png'))


def collate_value_add_self_values(df: pd.DataFrame,
                                  cols: list):
    """
    Convenience function for cleaning up the value add tables, customized for comparing dois and non-dois in source database
    Adapted from collate_value_add_values
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
            if col.startswith('dois'):
                columns_data.append(np.round(df[col] / df['num_dois'] * 100, 1))
            elif col.startswith('non_dois'):
                columns_data.append(np.round(df[col] / df['num_non_dois'] * 100, 1))

    added_columns = pd.DataFrame({name: data for name, data in zip(column_names, columns_data)})
    df = pd.concat([df, added_columns], axis=1)
    return df



## Tables

def generate_tables(af,
                    base_comparison: str = BASE_COMPARISON):

    table_json = {}
#    with pd.HDFStore(LOCAL_DATA_PATH) as store:
#        base_comparison_data = store[STORE_ELEMENT[base_comparison]]
    base_comparison_data = pd.read_csv(CSV_FILE[base_comparison])
    summary_table_df = pd.DataFrame(columns=['timeframe'] + ALL_COLLATED_COLUMNS)
    summary_source_table_df = pd.DataFrame(columns=['timeframe'] + ALL_COLLATED_COLUMNS)

    for timeframe in TIME_FRAMES.keys():
        filtered_comparison = base_comparison_data[base_comparison_data.published_year.isin(TIME_FRAMES[timeframe])]
        filtered_comparison_sum = filtered_comparison.sum(axis=0)
        filtered_comparison_sum['timeframe'] = timeframe
        summary_table_df = summary_table_df.append(filtered_comparison_sum, ignore_index=True)

    for source in SOURCES:
#        with pd.HDFStore(LOCAL_DATA_PATH) as store:
#            source_data = store[STORE_ELEMENT[source]]

        source_data = pd.read_csv(CSV_FILE[source])

        for timeframe in TIME_FRAMES.keys():
            filtered_source = source_data[source_data.published_year.isin(TIME_FRAMES[timeframe])]
            filtered_source_sum = filtered_source.sum(axis=0)
            filtered_source_sum['timeframe'] = timeframe
            summary_source_table_df = summary_source_table_df.append(filtered_comparison_sum, ignore_index=True)

        table_dict = generate_table_data(
            title=f'{FORMATTED_SOURCE_NAMES[source]} Metadata Coverage of Crossref DOIs',
            df=summary_table_df,
            columns=SUMMARY_TABLE_COLUMNS[source]['column_names'],
            short_column_names=SUMMARY_TABLE_COLUMNS[source]['nice_column_names'],
            identifier=None,
            sort_column=None
        )

        table_json[source] = {
            'summary_comparison_table': table_dict
        }

    for f in af.generate_file('tables.json'):
        json.dump(table_json, f)


if __name__ == '__main__':
    #crossref_to_truthtable(af='test',
    #                       rerun=False,
    #                       verbose=True)
    #openalex_to_truthtable(af='test',
    #                             rerun=False,
    #                             verbose=True)
    #dois_category_query(af='test',
    #                   rerun=False,
    #                    verbose=True)
    # source_category_query(af='test',
    #                      rerun=False,
    #                    verbose=True)
    pass
