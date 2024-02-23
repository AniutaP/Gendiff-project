#!/usr/bin/env python3
def make_indent(level):
    indent = '  '
    for i in range(level):
        indent += '    '
    return indent


def stringify(data, indent):
    if isinstance(data, dict):
        indent += '    '
        res = ['{']
        for key in data:
            value = stringify(data[key], indent)
            res.append(f'{indent}  {key}: {value}')
        res.append(indent[:-2] + '}')
        result = '\n'.join(res)
    elif data is None:
        result = 'null'
    elif type(data) is bool:
        result = str(data).lower()
    else:
        result = str(data)
    return result


def make_stylish(get_diff_list, level=0):  # noqa: C901
    result = ['{']
    indent = make_indent(level)

    for node in get_diff_list:
        if node['condition'] == 'children_node':
            data = make_stylish(node['children'], level + 1)
            result.append(f"{indent}  {node['name']}: {data}")
        if node['condition'] == 'unchanged':
            data = stringify(node['value'], indent)
            result.append(f"{indent}  {node['name']}: {data}")
        if node['condition'] == 'added':
            data = stringify(node['value'], indent)
            result.append(f"{indent}+ {node['name']}: {data}")
        if node['condition'] == 'deleted':
            data = stringify(node['value'], indent)
            result.append(f"{indent}- {node['name']}: {data}")
        if node['condition'] == 'updated':
            data = stringify(node['old_value'], indent)
            result.append(f"{indent}- {node['name']}: {data}")
            data = stringify(node['new_value'], indent)
            result.append(f"{indent}+ {node['name']}: {data}")
    result.append(indent[:-2] + '}')
    diff_list = '\n'.join(result)
    return diff_list


def stylish(get_diff_list):
    get_diff_list.sort(key=lambda x: x['name'])
    result = make_stylish(get_diff_list)
    return result
