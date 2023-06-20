#!/usr/bin/env python3
def plain(get_diff_list):
    get_diff_list.sort(key=lambda x: x['name'])
    result = make_plain(get_diff_list)
    return '\n'.join(result)


def make_plain(get_diff_list, path=''):
    result = []
    for node in get_diff_list:
        if node['condition'] == 'children_node':
            path_to_change = path + node['name'] + '.'
            difference = make_plain(node['children'], path_to_change)
            result.extend(difference)
        if node['condition'] == 'added':
            path_to_change = path + node['name']
            change = to_string(node['value'])
            difference = (
                f"Property '{path_to_change}' was added "
                f"with value: {change}"
            )
            result.append(difference)
        if node['condition'] == 'deleted':
            path_to_change = path + node['name']
            difference = f"Property '{path_to_change}' was removed"
            result.append(difference)
        if node['condition'] == 'updated':
            path_to_change = path + node['name']
            change_before = to_string(node['old_value'])
            change_after = to_string(node['new_value'])
            difference = (
                f"Property '{path_to_change}' was updated. "
                f'From {change_before} to {change_after}'
            )
            result.append(difference)
    return result


def to_string(data):
    if type(data) is dict or type(data) is list:
        result = '[complex value]'
    elif type(data) is bool:
        result = str(data).lower()
    elif data is None:
        result = 'null'
    elif type(data) is str:
        result = "'{}'".format(data)
    else:
        result = '{}'.format(data)
    return result
