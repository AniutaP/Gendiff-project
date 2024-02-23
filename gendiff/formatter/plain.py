#!/usr/bin/env python3
def make_string(data):
    if isinstance(data, dict):
        result = '[complex value]'
    elif data is None:
        result = 'null'
    elif type(data) is bool:
        result = f"{str(data).lower()}"
    else:
        result = f"'{str(data)}'"
    return result


def get_plain(get_diff_list, path=''):
    result = []
    for node in get_diff_list:
        path_to = ''.join([path, node['name']])
        if node['condition'] == 'children_node':
            path_to = ''.join([path_to, '.'])
            difference = get_plain(node['children'], path_to)
            result.extend(difference)
        if node['condition'] == 'added':
            value = make_string(node['value'])
            difference = (
                f"Property '{path_to}' was added "
                f"with value: {value}"
            )
            result.append(difference)
        if node['condition'] == 'deleted':
            path_to = path + node['name']
            difference = f"Property '{path_to}' was removed"
            result.append(difference)
        if node['condition'] == 'updated':
            path_to = path + node['name']
            old_value = make_string(node['old_value'])
            new_value = make_string(node['new_value'])
            difference = (
                f"Property '{path_to}' was updated. "
                f'From {old_value} to {new_value}'
            )
            result.append(difference)
    return result


def plain(get_diff_list):
    get_diff_list.sort(key=lambda x: x['name'])
    result = get_plain(get_diff_list)
    return '\n'.join(result)
