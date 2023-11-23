#!/usr/bin/env python3
def make_indent(level):
    indent = '  '
    for i in range(level):
        indent += '    '
    return indent


def stringify(data, indent):
    if isinstance(data, dict):
        indent += '    '
        result = '{\n'
        for key in data.keys():
            value = stringify(data[key], indent)
            result += f'{indent}  {key}: {value}\n'
        result += indent[:-2] + '}'
    elif data is None:
        result = 'null'
    elif type(data) is bool:
        result = str(data).lower()
    else:
        result = str(data)
    return result


def make_stylish(get_diff_list, level=0):  # noqa: C901
    result = '{\n'
    indent = make_indent(level)

    for node in get_diff_list:
        if node['condition'] == 'children_node':
            data = make_stylish(node['children'], level + 1)
            result += f"{indent}  {node['name']}: {data}\n"
        if node['condition'] == 'unchanged':
            data = stringify(node['value'], indent)
            result += f"{indent}  {node['name']}: {data}\n"
        if node['condition'] == 'added':
            data = stringify(node['value'], indent)
            result += f"{indent}+ {node['name']}: {data}\n"
        if node['condition'] == 'deleted':
            data = stringify(node['value'], indent)
            result += f"{indent}- {node['name']}: {data}\n"
        if node['condition'] == 'updated':
            data = stringify(node['old_value'], indent)
            result += f"{indent}- {node['name']}: {data}\n"
            data = stringify(node['new_value'], indent)
            result += f"{indent}+ {node['name']}: {data}\n"
    result += indent[:-2] + '}'

    return result


def stylish(get_diff_list):
    get_diff_list.sort(key=lambda x: x['name'])
    result = make_stylish(get_diff_list)
    return result
