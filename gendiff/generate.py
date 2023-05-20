#!/usr/bin/env python3
from gendiff.read_files import read_file
from gendiff.formatter.format import get_format


def generate_diff(file1, file2, formatter='stylish'):
    file_data_1 = read_file(file1)
    file_data_2 = read_file(file2)
    data_diff = get_diff(file_data_1, file_data_2)
    return get_format(data_diff, formatter)


def get_diff(file1_data, file2_data):
    in_second_but_not_in_first = list(set(file2_data) - set(file1_data))
    sort_keys = sorted(list(set(file1_data)) + in_second_but_not_in_first)
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
