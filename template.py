import os
from pathlib import Path
import logging

logging.basicConfig(
    level = logging.INFO,
    format = '[%(asctime)s]: %(message)s'
)

project_name = 'cnnClassifier'

list_of_folders = [
    '.github/workflows/.gitkeep',
    f'src/{project_name}/__init__.py',
    f'src/{project_name}/components/__init__.py',
    f'src/{project_name}/utils/__init__.py',
    f'src/{project_name}/config/__init__.py',
    f'src/{project_name}/pipeline/__init__.py',
    f'src/{project_name}/entity/__init__.py',
    f'src/{project_name}/constants__init__.py',
    'config/config.yaml',
    'params.yaml',
    'requirements.txt',
    'setup.py',
    'notebooks/trials.ipynb'
]

for path in list_of_folders:
    
    file_path = Path(path)
    
    # Separating out folders and files
    file_dir, file_name = os.path.split(file_path)

    # Creating directory
    if file_dir != "":
        os.makedirs(file_dir, exist_ok=True)
        logging.info(f'Creating Directory {file_dir}.')
    
    # Creating file
    if (not os.path.exists(file_path)) or (os.path.getsize(file_path) == 0):
        with open(file_path, 'w') as f:
            pass # Creating an empty file
        logging.info(f'Creating file {file_name}')
    else:
        logging.info(f'File {file_name} already exists.')