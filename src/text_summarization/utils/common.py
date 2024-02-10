import os
import yaml
from pathlib import Path
from typing import Any

from src.text_summarization.logger import logging

from box.exceptions import BoxValueError
from box import ConfigBox
from ensure import ensure_annotations


# TO READ YAML FILES
@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    '''
    Args:-  path_to_yaml: path like input
    Return:-  ConfigBox: ConfigBox type
    Raise:-  ValueError: If yaml file is empty
             e: empty
    '''

    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logging.info(f"yaml_file: {path_to_yaml} loaded successfull")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")  
    except Exception as e:
        raise e
    

# To Create Directories
@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logging.info(f"created directory at {path}")
        else:
            pass

# To Get the size of a file
def get_size(path: Path) -> str:
    size = round(os.path.getsize(path)/1024)  # Size in kb
    return f"~ {size} KB" 


