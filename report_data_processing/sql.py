# MAG Metadata Coverage Report
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
# Authors: Cameron Neylon, Bianca Kramer

# SQL Queries used for interacting with the BigQuery Datasets

# Document Types and Counts

from pathlib import Path
from typing import Union, Optional

SQL_DIRECTORY = Path("report_data_processing/sql")

def load_sql_to_string(filepath: Union[str, Path],
                       parameters: Optional[dict]=None,
                       directory: Optional[Union[str, Path]]=None):

    filepath = Path(filepath)
    if directory:
        filepath = Path(directory) / filepath

    #assert (filepath.suffix == '.sql') or (filepath.suffix == 'jinja2')

    with open(filepath, 'r') as f:
        sql = f.readlines()

    sql_string = "".join(sql)

    if parameters:
        sql_string = sql_string.format(**parameters)

    return sql_string


# Example
# Metadata Elements and MAG Added Value to Crossref
# doi_table_categories_query = load_sql_to_string("doi_table_categories_query.sql",
                                                # directory=SQL_DIRECTORY)


