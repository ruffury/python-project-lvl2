import json
from typing import Dict


def get_data(file_path: str) -> Dict:
    """
    Return dict from parsed json file from file_path.

    Parameters:
        file_path: path to file

    Returns:
        the data in file.
    """
    with open(file_path, 'r') as file_data:
        data_dict = json.load(file_data)
    return data_dict
