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

from observatory.reports import report_utils
from precipy.analytics_function import AnalyticsFunction
from report_data_processing.sql import (
    hello_world
)

# Insert applicable graphs once created
# from report_graphs import (
#     Alluvial, OverallCoverage, BarLine, ValueAddBar, ValueAddByCrossrefType, ValueAddByCrossrefTypeHorizontal,
#     PlotlyTable
# )

# Replace with applicable project name
PROJECT_ID = 'coki-curtin-research-qualities'


def get_data(af: AnalyticsFunction,
             rerun: bool = False,
             verbose: bool = True):
    """
    Template function for downloading data from BigQuery

    Change 'query', 'project_id' and output filenames
    """

    if verbose:
        print(f'Running {af.function_name}...')
    if not rerun:
        if verbose:
            print(f'...not running query, rerun: {rerun}')
        return

    hello_world_query = pd.read_gbq(query=hello_world,
                                    project_id=PROJECT_ID)

    hello_world_query.to_csv('hello_world.csv')
    af.add_existing_file('hello_world.csv')
    if verbose:
        print('...completed')


def make_bq_table(af: AnalyticsFunction,
                  rerun: bool = False,
                  verbose: bool = True):
    """
    Template function for running a query remotely and saving the new table in BigQuery
    """

    if verbose:
        print(f'Running {af.function_name}...')
    if not rerun:
        if verbose:
            print(f'...not running query, rerun: {rerun}')
        return

    print('Generating the ROC DOI Table')
    with bigquery.Client() as client:
        job_config = bigquery.QueryJobConfig(destination=DESTINATION_TABLE,
                                             create_disposition='CREATE_IF_NEEDED',
                                             write_disposition='WRITE_TRUNCATE')

        # Start the query, passing in the extra configuration.
        query_job = client.query(QUERY, job_config=job_config)  # Make an API request.
        query_job.result()  # Wait for the job to complete.

    if verbose:
        print('...completed')


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