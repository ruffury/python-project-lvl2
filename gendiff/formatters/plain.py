ADDED = "Property '{0}' was added with value: {1}"
REMOVED = "Property '{0}' was removed"
UPDATED = "Property '{0}' was updated. From {1} to {2}"

STATUS = 'status'


def format_plain(diff):
    plain_diff = []
    for diff_key, diff_value in sorted(flatten(diff).items()):
        if diff_value[STATUS] == 'added':
            plain_diff.append(ADDED.format(diff_key, fmt_value(diff_value['value'])))
        if diff_value[STATUS] == 'removed':
            plain_diff.append(REMOVED.format(diff_key))
        elif diff_value[STATUS] == 'updated':
            node_old_value = fmt_value(diff_value['old_value'])
            node_new_value = fmt_value(diff_value['new_value'])
            plain_diff.append(UPDATED.format(diff_key, node_old_value, node_new_value))
    return '\n'.join(plain_diff)


def flatten(node, prefix='', flat=None):
    flatted_node = {} if flat is None else flat
    for node_key, node_value in node.items():
        new_key = '{0}.{1}'.format(prefix, node_key) if prefix else node_key
        if node_value[STATUS] == 'nested':
            flatten(node_value['children'], new_key, flatted_node)
        else:
            flatted_node[new_key] = node_value
    return flatted_node


def fmt_value(value):
    if isinstance(value, dict):
        return '[complex value]'
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    if isinstance(value, str):
        return "'{0}'".format(value)
    return str(value)
