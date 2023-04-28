#!/usr/bin/env python3
import json
import itertools


def generate_diff(first_file, second_file):
    file1_data = json.load(first_file)
    file2_data = json.load(second_file)
    data = []
    for key in file1_data:
        if key not in file2_data:
            data.append(f' - {key}: {file1_data[key]}')
        elif file1_data[key] == file2_data[key]:
            data.append(f'   {key}: {file1_data[key]}')
        else:
            data.append(f' - {key}: {file1_data[key]}')
            data.append(f' + {key}: {file2_data[key]}')
    for key in file2_data:
        if key not in file1_data:
            data.append(f' + {key}: {file2_data[key]}')

    result = itertools.chain("{", sorted(data, key=lambda x: x[3]), "}")
    print('\n'.join(result))
    return '\n'.join(result)
