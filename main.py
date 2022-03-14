import shutil
import json
from pathlib import Path
from precipy.main import render_file

import data_process
import graphs
import data_parameters
import graph_parameters

# Run precipy
render_file('config.json', [data_process, graphs], storages=[])

# Make a dated archive of the output files
output_store_path = Path('reports') / f'run_{data_parameters.TODAY_STR}'
precipy_output_path = Path('output_files')

n = 2
while output_store_path.exists():
    output_store_path = Path('reports') / f'run_{data_parameters.TODAY_STR}_{str(n)}'
    n = n + 1

shutil.copytree(precipy_output_path, output_store_path, shutil.copy2)
