LF_CHAR = '\n'
INDENT_CHAR = ' '
INDENT_STEP = 4

get_status_sign = {
    'added': '+ ',
    'removed': '- ',
}.get


def format_stylish(diff, indent=0):
    stylish_diff = []
    for diff_key, diff_value in sorted(diff.items()):
        new_indent = indent + INDENT_STEP
        if diff_value['status'] == 'updated':
            node_value = format_value(diff_value['old_value'], new_indent)
            stylish_diff.append(add_prefix(new_indent, 'removed', diff_key, node_value))
            node_value = format_value(diff_value['new_value'], new_indent)
            stylish_diff.append(add_prefix(new_indent, 'added', diff_key, node_value))
            continue
        if diff_value['status'] == 'nested':
            node_value = format_stylish(diff_value['children'], new_indent)
        else:
            node_value = format_value(diff_value['value'], new_indent)
        stylish_diff.append(add_prefix(
            indent=new_indent,
            status=diff_value['status'],
            node_key=diff_key,
            node_value=node_value,
        ),
        )
    return compose_stylish(indent, stylish_diff)


def format_value(value, indent):
    if isinstance(value, dict):
        stylish_value = []
        for node_key, node_value in value.items():
            new_indent = indent + INDENT_STEP
            value = format_value(node_value, new_indent)
            stylish_value.append(add_prefix(new_indent, None, node_key, value))
        return compose_stylish(indent, stylish_value)
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    return str(value)


def add_prefix(indent, status, node_key, node_value):
    prefix = LF_CHAR + INDENT_CHAR * indent
    status_sign = get_status_sign(status)
    if status_sign:
        prefix = prefix[:-2] + status_sign
    return '{0}{1}: {2}'.format(prefix, node_key, node_value)


def compose_stylish(indent, output):
    return '{{{0}}}'.format(''.join(output) + LF_CHAR + INDENT_CHAR * indent)
