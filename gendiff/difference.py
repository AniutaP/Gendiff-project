#!/usr/bin/env python3
def get_diff(entry_data1, entry_data2):
    sort_keys = sorted(entry_data1.keys() | entry_data2.keys())
    diff = []

    for key in sort_keys:
        node = {'name': key}
        if key not in entry_data2:
            node['condition'] = 'deleted'
            node['value'] = entry_data1[key]
        elif key not in entry_data1:
            node['condition'] = 'added'
            node['value'] = entry_data2[key]
        elif isinstance(entry_data1[key], dict) \
                and isinstance(entry_data2[key], dict):
            node['condition'] = 'children_node'
            node['children'] = get_diff(entry_data1[key], entry_data2[key])
        elif entry_data1[key] != entry_data2[key]:
            node['condition'] = 'updated'
            node['old_value'] = entry_data1[key]
            node['new_value'] = entry_data2[key]
        else:
            node['condition'] = 'unchanged'
            node['value'] = entry_data1[key]
        diff.append(node)
    return diff
