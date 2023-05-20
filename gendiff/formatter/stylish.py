#!/usr/bin/env python3
def stylish(get_diff_list, level=0):
    result = '{\n'
    indent = '  '

    for i in range(level):
        indent += '    '

    get_diff_list.sort(key=lambda x: x['name'])

    for node in get_diff_list:
        if node['condition'] == 'children_node':
            data = stylish(node['children'], level + 1)
            result += f"{indent}  {node['name']}: {data}\n"
        elif node['condition'] == 'unchanged':
            data = stringify(node['value'], indent)
            result += f"{indent}  {node['name']}: {data}\n"
        elif node['condition'] == 'added':
            data = stringify(node['value'], indent)
            result += f"{indent}+ {node['name']}: {data}\n"
        elif node['condition'] == 'deleted':
            data = stringify(node['value'], indent)
            result += f"{indent}- {node['name']}: {data}\n"
        else:
            data = stringify(node['old_value'], indent)
            result += f"{indent}- {node['name']}: {data}\n"
            data = stringify(node['new_value'], indent)
            result += f"{indent}+ {node['name']}: {data}\n"
    result += indent[:-2] + '}'

    return result


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
