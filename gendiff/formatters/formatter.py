from gendiff.formatters.json import format_json
from gendiff.formatters.plain import format_plain
from gendiff.formatters.stylish import format_stylish

formatters = {
    'json': format_json,
    'stylish': format_stylish,
    'plain': format_plain,
}


def format_diff(diff, style):
    return formatters.get(style)(diff)
