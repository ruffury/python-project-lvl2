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
    return json.dumps(dictionary)
