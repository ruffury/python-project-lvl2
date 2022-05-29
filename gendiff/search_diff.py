TREE_VALUE = 'value'
STATUS = 'status'

ADDED = 'added'
UPDATED = 'updated'
REMOVED = 'removed'
NOT_CHANGED = 'not_changed'
NESTED = 'nested'


def get_value(dict1, dict2, key):
    value1 = dict1[key]
    value2 = dict2[key]
    if isinstance(value1, dict) and isinstance(value2, dict):
        return {
            STATUS: NESTED,
            'children': search_diff(value1, value2),
        }
    elif value1 == value2:
        return {
            STATUS: NOT_CHANGED,
            TREE_VALUE: value1,
        }
    return {
        STATUS: UPDATED,
        'old_{0}'.format(TREE_VALUE): value1,
        'new_{0}'.format(TREE_VALUE): value2,
    }


def search_diff(dict1, dict2):
    keys1 = dict1.keys()
    keys2 = dict2.keys()
    difference = {}
    for key in sorted(keys1 & keys2):
        difference[key] = get_value(dict1, dict2, key)
    for key in sorted(keys1 - keys2):
        difference[key] = {
            STATUS: REMOVED,
            TREE_VALUE: dict1[key],
        }
    for key in sorted(keys2 - keys1):
        difference[key] = {
            STATUS: ADDED,
            TREE_VALUE: dict2[key],
        }

    return difference
