from gendiff.formatters.json import format_json
from gendiff.formatters.stylish import format_stylish

formatters = {
    'json': format_json,
    'stylish': format_stylish,
}


def format_diff(diff, style):
    return formatters.get(style)(diff)
