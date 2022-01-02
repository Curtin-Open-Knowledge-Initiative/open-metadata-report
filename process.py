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
# Authors: COKI Team
import json
import requests
from pathlib import Path
import os

import pandas as pd
import numpy as np
import plotly.graph_objects as go
from typing import Optional, Callable, Union

from google.cloud import bigquery
from git import Repo

from observatory.reports import report_utils
from precipy.analytics_function import AnalyticsFunction
from report_data_processing.sql import load_sql_to_string
from parameters import *


def source_to_intermediate(af: AnalyticsFunction,
                           source: str,
                           rerun: bool = RERUN,
                           verbose: bool = VERBOSE):
    """
    Generate the intermediate table from source data
    """

    if verbose:
        print(f'Running {af.function_name} with source: {source}...')
    if not rerun:
        if verbose:
            print(f'...not running query, rerun: {rerun}')
        return

    query = load_sql_to_string('source_to_intermediate.sql',
                               parameters=dict(
                                   tables=TABLES[source]
                               ),
                               directory=SQL_DIRECTORY
                               )
    destination_table = INTERMEDIATE_TABLES[source]

    with bigquery.Client() as client:
        job_config = bigquery.QueryJobConfig(destination=destination_table,
                                             create_disposition='CREATE_IF_NEEDED',
                                             write_disposition='WRITE_TRUNCATE')

        # Start the query, passing in the extra configuration.
        query_job = client.query(query, job_config=job_config)  # Make an API request.
        query_job.result()  # Wait for the job to complete.

    if verbose:
        print('...completed')


def create_qdoi_table(af: AnalyticsFunction,
                      rerun: bool = RERUN,
                      verbose: bool = VERBOSE):
    """
    Generate a 'doi-like' table containing the elements from crossref, openalex and mag for analysis
    """

    if not report_utils.bigquery_rerun(af, rerun, verbose):
        return

    query = load_sql_to_string('create_q_doi_table.sql',
                               parameters=dict(
                                   doi_table=TABLES['crossref'],
                                   intermediate_tables=INTERMEDIATE_TABLES
                               ),
                               directory=SQL_DIRECTORY
                               )

    with bigquery.Client() as client:
        job_config = bigquery.QueryJobConfig(destination=Q_DOI_TABLE,
                                             create_disposition='CREATE_IF_NEEDED',
                                             write_disposition='WRITE_TRUNCATE')

        # Start the query, passing in the extra configuration.
        query_job = client.query(query, job_config=job_config)  # Make an API request.
        query_job.result()  # Wait for the job to complete.

    if verbose:
        print('...completed')


def query_intermediates_categories(af: AnalyticsFunction,
                                   source: str,
                                   rerun: bool = RERUN,
                                   verbose: bool = VERBOSE):
    """
    Query and download category data from the intermediate tables
    """

    if verbose:
        print(f'Running {af.function_name} with source: {source}...')
    if not rerun:
        if verbose:
            print(f'...not running query, rerun: {rerun}')
        return

    query = load_sql_to_string('intermediates_categories_query.sql',
                               parameters=dict(table=INTERMEDIATE_TABLES[source]),
                               directory=SQL_DIRECTORY)

    categories = pd.read_gbq(query=query,
                             project_id=PROJECT_ID)

    with pd.HDFStore(LOCAL_DATA) as store:
        store[f'{source}_categories'] = categories


def query_qdoi_categories(af: AnalyticsFunction,
                          rerun: bool = RERUN,
                          verbose: bool = VERBOSE):
    """
    Query and download category data from the quasi doi table
    """

    if not report_utils.bigquery_rerun(af, rerun, verbose):
        return

    query = load_sql_to_string('doi_categories_query.sql',
                               parameters=dict(
                                   crossref_member_table=CROSSREF_MEMBER_DATA_TABLE,
                                   qdoi_table=Q_DOI_TABLE),
                               directory=SQL_DIRECTORY)

    categories = pd.read_gbq(query=query,
                             project_id=PROJECT_ID)

    with pd.HDFStore(LOCAL_DATA) as store:
        store[f'doi_categories'] = categories

    if verbose:
        print('...completed')


def crossref_member_status(af: AnalyticsFunction,
                           push_to_gbq: bool = False,
                           if_exists: str = 'fail'):
    """
    Poll the Crossref Member API for data on the abstracts and citations status of a member
    """

    cursor = '*'

    total_results = 500
    results_received = 0

    l = []
    while results_received < total_results:
        r = requests.get('http://api.crossref.org/members/',
                         params=dict(cursor=cursor,
                                     rows=500,
                                     mailto='cn@cameronneylon.net'))
        r.raise_for_status()
        j = r.json()
        total_results = j['message']['total-results']
        results_received = results_received + len(j['message']['items'])
        cursor = j['message']['next-cursor']

        l.extend([
            dict(
                id=item['id'],
                primary_name=item['primary-name'],
                prefix=prefix_data['value'],
                name=prefix_data['name'],
                public_references=prefix_data['public-references'],
                collection_date=TODAY
            )
            for item in j['message']['items']
            for prefix_data in item['prefix']
        ])
        print(f'{results_received} results so far...')

    df = pd.DataFrame(columns=['id', 'primary_name', 'prefix', 'name', 'public_references', 'collection_date'],
                      data=l)
    df.drop_duplicates(inplace=True)

    df.to_csv(f'crossref_member_data{TODAY_STR}.csv', index=False)

    if push_to_gbq:
        client = bigquery.Client(project=PROJECT_ID)

        # Table needs to exist to be able to do this partitioned load
        job_config = bigquery.LoadJobConfig(
            write_disposition="WRITE_TRUNCATE",
        )

        # Include target partition in the table id:
        job = client.load_table_from_dataframe(df,
                                               destination=CROSSREF_MEMBER_DATA_TABLE,
                                               job_config=job_config)  # Make an API request
        job.result()  # Wait for job to finish


def git_status(af):
    """
    Record Git Status for Current State of the Repo
    """

    repo = Repo(search_parent_directories=True)
    print('This report was run from the git commit hash: ' + repo.head.object.hexsha)
    changedfiles = [item.a_path for item in repo.index.diff(None)]
    if len(changedfiles > 0):
        print('WARNING: This report was run with local changes that were not committed to the following files: ')
        print(changedfiles)

    for f in af.generate_file('git_status.json'):
        json.dump(dict(
            sha=repo.head.object.hexsha,
            changedfiles=[item.a_path for item in repo.index.diff(None)],
            branch=repo.active_branch.name),
            f
        )


## TESTING

if __name__ == '__main__':
    crossref_member_status('af',
                           push_to_gbq=True)
