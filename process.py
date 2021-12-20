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
from pathlib import Path
import os

import pandas as pd
import numpy as np
import plotly.graph_objects as go
from typing import Optional, Callable, Union

from google.cloud import bigquery

from observatory.reports import report_utils
from precipy.analytics_function import AnalyticsFunction
from report_data_processing.sql import load_sql_to_string
from parameters import *


def source_to_intermediate(af: AnalyticsFunction,
                           source: str,
                           selector: str,
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
                                   tables=TABLES[source],
                                   selector=SELECTOR[selector][source]
                               ),
                               directory=SQL_DIRECTORY
                               )
    destination_table = INTERMEDIATE_TABLES[source][selector]

    with bigquery.Client() as client:
        job_config = bigquery.QueryJobConfig(destination=destination_table,
                                             create_disposition='CREATE_IF_NEEDED',
                                             write_disposition='WRITE_TRUNCATE')

        # Start the query, passing in the extra configuration.
        query_job = client.query(query, job_config=job_config)  # Make an API request.
        query_job.result()  # Wait for the job to complete.

    if verbose:
        print('...completed')


def query_intermediate(af: AnalyticsFunction,
                       source: str,
                       selector: str,
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

    query = load_sql_to_string('intermediate_category_query.sql',
                               parameters=dict(table=INTERMEDIATE_TABLES[source][selector]),
                               directory=SQL_DIRECTORY)

    categories = pd.read_gbq(query=query,
                             project_id=PROJECT_ID)

    with pd.HDFStore(LOCAL_DATA) as store:
        store[f'{source}_{selector}_categories'] = categories


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
