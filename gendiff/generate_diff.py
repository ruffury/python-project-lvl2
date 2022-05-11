from gendiff.file_parser import get_data
from gendiff.formatters.json import format_json
from gendiff.search_diff import search_diff


def generate_diff(first_file: str, second_file: str) -> str:
    """
    Return difference in data between two files.

    Parameters:
        first_file: path to first file
        second_file: path to second_file

    Returns:
        string as difference between data.
    """
    first_dict = get_data(first_file)
    second_dict = get_data(second_file)

    difference = search_diff(first_dict, second_dict)

    return format_json(difference)
