import os
from box.exceptions import BoxValueError
import yaml
from Swayam_TextSummarization.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

@ensure_annotations #decorator to ensure type hints are met
def read_yaml(path_to_yaml:Path) -> ConfigBox:
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"Successfully loaded YAML file: {path_to_yaml}")
            return ConfigBox(content)
    except BoxValueError:
        raise BoxValueError(f"The file {path_to_yaml} does not exist.")
    except Exception as e:
        logger.error(f"Error reading YAML file: {e}")
        raise e


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """
    Create directories if they do not exist.
    Args:
        path_to_directories (list): List of directories to create.
        verbose (bool): Whether to print the directory creation status.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory: {path}") if os.path.exists(path) else logger.info(f"Directory already exists: {path}")


@ensure_annotations
def get_size(path:Path)->str:
    """
    Get the size of a directory or file.
    Args:
        path (Path): Path to the directory or file.
    Returns:
        str: Size in bytes.
    """
    size_in_kb=round(os.path.getsize(path)/1024)
    return f"{size_in_kb} KB"