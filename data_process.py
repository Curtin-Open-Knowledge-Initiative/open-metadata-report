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
from google.cloud import bigquery
from git import Repo

from observatory.reports import report_utils
from precipy.analytics_function import AnalyticsFunction
from report_data_processing.sql import load_sql_to_string
from data_parameters import *


def source_to_intermediate(af: AnalyticsFunction,
                           rerun: bool = RERUN,
                           verbose: bool = VERBOSE):
    """
    Generate the intermediate table from source data
    """

    for source in MAG_FORMAT_SOURCES:
        query = load_sql_to_string('source_to_intermediate.sql',
                                   parameters=TABLES[source],
                                   directory=SQL_DIRECTORY
                                   )
        destination_table = INTERMEDIATE_TABLES[source]

        if not report_utils.bigquery_rerun(af, rerun, verbose, source):
            print(f"""Query String is:
            
    {query}
    
    """)
            print(f'Destination Tables is:{destination_table}')
            continue

        with bigquery.Client() as client:
            job_config = bigquery.QueryJobConfig(destination=destination_table,
                                                 create_disposition='CREATE_IF_NEEDED',
                                                 write_disposition=WRITE_DISPOSITION)

            # Start the query, passing in the extra configuration.
            query_job = client.query(query, job_config=job_config)  # Make an API request.
            query_job.result()  # Wait for the job to complete.

        if verbose:
            print('...completed')


def intermediate_to_source_truthtable(af: AnalyticsFunction,
                                      rerun: bool = RERUN,
                                      verbose: bool = VERBOSE):
    """
    Query and download category data from the intermediate tables
    """

    for source in MAG_FORMAT_SOURCES:
        query = load_sql_to_string('intermediates_truthtable_query.sql',
                                   parameters=dict(
                                       table=INTERMEDIATE_TABLES[source],
                                       openalex_additional_fields=TABLES[source]['openalex_additional_truthtable_fields']
                                   ),
                                   directory=SQL_DIRECTORY)

        if not report_utils.bigquery_rerun(af, rerun, verbose, source):
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


def openalex_native_to_truthtable(af: AnalyticsFunction,
                                  source: str='openalex_native',
                                  rerun: bool = RERUN,
                                  verbose: bool = VERBOSE):
    """
    Convert OpenAlex Native Format Works Table to Truthtable

    Note that OpenAlex uses the fully qualified URL form of the doi in lower case and needs conversion.
    See the query for details.
    """

    query = load_sql_to_string('openalex_native_truthtable.sql',
                               parameters=dict(table=TABLES[source]['Work']),
                               directory=SQL_DIRECTORY)

    if not report_utils.bigquery_rerun(af, rerun, verbose, source):
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

def crossref_to_truthtable(af: AnalyticsFunction,
                           source: str = 'crossref',
                           rerun: bool = RERUN,
                           verbose: bool = VERBOSE):
    """
    Calculate truthtable for Crossref
    """

    query = load_sql_to_string('crossref_truthtable_query.sql',
                               parameters=dict(table=TABLES[source],
                                               crossref_member_table=CROSSREF_MEMBER_DATA_TABLE,
                                               crossref_member_date=CROSSREF_MEMBER_DATE),
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

    for source in [s for s in SOURCES if s !='crossref']:
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
            return

        categories = pd.read_gbq(query=query,
                                 project_id=PROJECT_ID)

        with pd.HDFStore(LOCAL_DATA_PATH) as store:
            store[STORE_ELEMENT[source]] = categories

        categories.to_csv(CSV_FILE[source])

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

    with pd.HDFStore(LOCAL_DATA_PATH) as store:
        store[STORE_ELEMENT['crossref']] = categories

    categories.to_csv(CSV_FILE['crossref'])
    if verbose:
        print('...completed')


def crossref_member_status(af: AnalyticsFunction,
                           push_to_gbq: bool = True,
                           if_exists: str = 'fail',
                           rerun=RERUN):
    """
    Poll the Crossref Member API for data on the abstracts and citations status of a member
    """

    print('Running crossref memberdata collection...')

    # Skip running the Crossref API if directed not to or the data should (in theory) already exist
    if (rerun is False) or (CROSSREF_MEMBER_DATE != TODAY.isoformat()):
        print('Skipisping poking the Crossref Member API')
        return

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

    df.to_csv(DATA_DIR / f'crossref_member_data{TODAY_STR}.csv', index=False)

    if push_to_gbq:
        client = bigquery.Client(project=PROJECT_ID)

        # Table needs to exist to be able to do this partitioned load
        job_config = bigquery.LoadJobConfig(
            write_disposition="WRITE_APPEND",
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


## TESTING

if __name__ == '__main__':
    # source_to_intermediate(af="test",
    #                        rerun=False,
    #                        verbose=True)
    # source_to_intermediate(af="test",
    #                        rerun=False,
    #                        verbose=True)
    # crossref_to_truthtable(af='test',
    #                       rerun=False,
    #                       verbose=True)
    # intermediate_to_source_truthtable(af="test",
    #                        rerun=False,
    #                        verbose=True)
    # intermediate_to_source_truthtable(af="test",
    #                        rerun=False,
    #                        verbose=True)
    # dois_category_query(af='test',
    #                     rerun=False,
    #                     verbose=True)
    # source_category_query(af='test',
    #                       rerun=False,
    #                       verbose=True)
    # openalex_native_to_truthtable(af='test',
    #                               rerun=False,
    #                               verbose=True)
    pass
