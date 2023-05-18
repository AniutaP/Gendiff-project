#!/usr/bin/env python3
import itertools
from gendiff.read_files import read_file


def generate_diff(file1, file2):
    file_data_1 = read_file(file1)
    file_data_2 = read_file(file2)
    data_diff = get_diff(file_data_1, file_data_2)
    res = itertools.chain("{", data_diff, "}")
    return data_diff


def get_diff(file1_data, file2_data):
    in_second_but_not_in_first = list(set(file2_data) - set(file1_data))
    sort_keys = sorted(list(set(file1_data)) + in_second_but_not_in_first)
    data = []

    for key in sort_keys:
        if key not in file2_data:
            data.append(f' - {key}: {file1_data[key]}')
        elif key not in file1_data:
            data.append(f' + {key}: {file2_data[key]}')
        elif isinstance(file1_data[key], dict) and isinstance(file2_data[key], dict):
            children = get_diff(file1_data[key], file2_data[key])
            data.append(children)
        elif file1_data[key] != file2_data[key]:
            data.append(f' - {key}: {file1_data[key]}')
            data.append(f' + {key}: {file2_data[key]}')
        else:
            data.append(f'   {key}: {file1_data[key]}')

    return data
