#!/usr/bin/env python
import json


def json_to_str(value):
    if isinstance(value, bool):
        if value:
            return 'true'
        else:
            return 'false'
    return value


def generate_diff(file_path1: str, file_path2: str) -> str:
    json1 = json.load(open(file_path1))
    json2 = json.load(open(file_path2))

    json_keys1, json_keys2 = set(json1), set(json2)

    union_keys = sorted(json_keys1.union(json_keys2))

    result = '{\n'
    for key in union_keys:
        if key in json_keys1 and key in json_keys2:
            if json1[key] == json2[key]:
                result += f'    {key}: {json_to_str(json1[key])}\n'
            else:
                result += f'  - {key}: {json_to_str(json1[key])}\n'
                result += f'  + {key}: {json_to_str(json2[key])}\n'
        elif key in json_keys1 and key not in json_keys2:
            result += f'  - {key}: {json_to_str(json1[key])}\n'
        else:
            result += f'  + {key}: {json_to_str(json2[key])}\n'
    result += '}'

    return result
