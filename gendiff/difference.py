#!/usr/bin/env python3
def get_diff(file1_data, file2_data):
    sort_keys = sorted(file1_data.keys() | file2_data.keys())
    data = []

    for key in sort_keys:
        node = {'name': key}
        if key not in file2_data:
            node['condition'] = 'deleted'
            node['value'] = file1_data[key]
        elif key not in file1_data:
            node['condition'] = 'added'
            node['value'] = file2_data[key]
        elif isinstance(file1_data[key], dict) \
                and isinstance(file2_data[key], dict):
            node['condition'] = 'children_node'
            node['children'] = get_diff(file1_data[key], file2_data[key])
        elif file1_data[key] != file2_data[key]:
            node['condition'] = 'updated'
            node['old_value'] = file1_data[key]
            node['new_value'] = file2_data[key]
        else:
            node['condition'] = 'unchanged'
            node['value'] = file1_data[key]
        data.append(node)
    return data
