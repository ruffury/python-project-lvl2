import json
from typing import Dict


def format_json(dictionary: Dict) -> str:
    """
    Return string as data from dict.

    Parameters:
        dictionary: data to format

    Returns:
        the string of data
    """
    result_string = json.dumps(dictionary, indent=2).replace(',', '')
    return ''.join(result_string.split('"'))
