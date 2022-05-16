import json
import os
from typing import Dict

import yaml


def get_data(file_path: str) -> Dict:
    """
    Return dict from parsed json file from file_path.

    Parameters:
        file_path: path to file

    Returns:
        the data in file.
    """
    _, file_extension = os.path.splitext(file_path)
    with open(file_path, 'r') as file_data:
        if file_extension == '.json':
            data_dict = json.load(file_data)
        elif file_extension in {'.yml', '.yaml'}:
            data_dict = yaml.safe_load(file_data)
    return data_dict
