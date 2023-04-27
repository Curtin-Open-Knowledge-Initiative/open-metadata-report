import shutil
import json
from pathlib import Path
from precipy.main import render_file

import data_process

precipy_config_file = 'config.json'

# Run precipy
render_file(precipy_config_file, [data_process], storages=[])

# Make a dated archive of the output files
with open(precipy_config_file) as f:
    precipy_output_path = Path(json.load(f).get('output_bucket_name'))

with open(precipy_output_path / 'data_parameters.json') as f:
    output_store_path = Path(json.load(f).get('ARCHIVE_REPORT_DIR'))

if output_store_path.exists():
    print(
f"""
The output directory {output_store_path} already exists. 

For safety reasons an archive copy will not be made. Your most recent run is available in '{precipy_output_path}'.
"""
    )

else:
    shutil.copytree(precipy_output_path, output_store_path, shutil.copy2)
