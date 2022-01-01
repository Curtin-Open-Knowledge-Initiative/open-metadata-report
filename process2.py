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
#from git import Repo

from observatory.reports import report_utils
from precipy.analytics_function import AnalyticsFunction
from report_data_processing.sql import load_sql_to_string
from parameters import *


def crossref_member_status(af: AnalyticsFunction,
                           push_to_gbq: bool = True,
                           #push_to_gbq: bool = False,
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


## TESTING

#if __name__ == '__main__':
#    crossref_member_status('af',
#                           push_to_gbq=True)