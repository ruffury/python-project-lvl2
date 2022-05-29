from gendiff.file_parser import get_data
from gendiff.formatters.formatter import format_diff
from gendiff.search_diff import search_diff


def generate_diff(first_file: str, second_file: str, format_type='stylish') -> str:
    """
    Return difference in data between two files.

    Parameters:
        first_file: path to first file
        second_file: path to second_file
        format_type: type of style

    Returns:
        string as difference between data.
    """
    first_dict = get_data(first_file)
    second_dict = get_data(second_file)

    difference = search_diff(first_dict, second_dict)

    return format_diff(difference, format_type)
