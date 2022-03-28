import shutil
import json
from pathlib import Path
from precipy.main import render_file

import data_process
import data_parameters

# Run precipy
render_file('config.json', [data_process], storages=[])

# Make a dated archive of the output files
output_store_path = Path('reports') / f'run_{data_parameters.TODAY_STR}'
precipy_output_path = Path('output_files')

with open(precipy_output_path / 'data_parameters.json') as f:
    params = json.load(f)

output_store_path = Path(params.get('ARCHIVE_REPORT_DIR'))

if output_store_path.exists():
    print(
f"""
The output directory {output_store_path} already exists. 

For safety reasons an archive copy will not be made. Your most recent run is available in 'output_files'.
"""
    )

else:
    shutil.copytree(precipy_output_path, output_store_path, shutil.copy2)
