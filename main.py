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
shutil.copytree(precipy_output_path, output_store_path, shutil.copy2)

# Write out parameter sets to run archive folder
with open(output_store_path / 'data_parameters.json', 'w') as f:
    json.dump({item: getattr(data_parameters, item) for item in dir(data_parameters) if not item.startswith('__')},
              f,
              default=str)
with open(output_store_path / 'graph_parameters.json', 'w') as f:
    json.dump({item: getattr(graph_parameters, item) for item in dir(graph_parameters) if not item.startswith('__')},
              f,
              default=str)
