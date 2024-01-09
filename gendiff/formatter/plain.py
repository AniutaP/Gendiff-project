#!/usr/bin/env python3
def make_string(data):
    data_type = {dict: '[complex value]',
                 list: '[complex value]',
                 bool: str(data).lower(),
                 str: "'{}'".format(data),
                 }
    if type(data) in data_type:
        result = data_type[type(data)]
    elif data is None:
        result = 'null'
    else:
        result = data
    return result


def make_plain(get_diff_list, path=''):
    result = []
    for node in get_diff_list:
        if node['condition'] == 'children_node':
            path_to_difference = path + node['name'] + '.'
            difference = make_plain(node['children'], path_to_difference)
            result.extend(difference)
        if node['condition'] == 'added':
            path_to_difference = path + node['name']
            value = make_string(node['value'])
            difference = (
                f"Property '{path_to_difference}' was added "
                f"with value: {value}"
            )
            result.append(difference)
        if node['condition'] == 'deleted':
            path_to_difference = path + node['name']
            difference = f"Property '{path_to_difference}' was removed"
            result.append(difference)
        if node['condition'] == 'updated':
            path_to_difference = path + node['name']
            old_value = make_string(node['old_value'])
            new_value = make_string(node['new_value'])
            difference = (
                f"Property '{path_to_difference}' was updated. "
                f'From {old_value} to {new_value}'
            )
            result.append(difference)
    return result


def plain(get_diff_list):
    get_diff_list.sort(key=lambda x: x['name'])
    result = make_plain(get_diff_list)
    return '\n'.join(result)
