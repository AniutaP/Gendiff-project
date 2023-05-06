#!/usr/bin/env python3
import itertools
from gendiff.read_files import read_file


def generate_diff(file1, file2):
    file1_data = read_file(file1)
    file2_data = read_file(file2)
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
    data_lower = [x.lower() for x in data]
    res = itertools.chain("{", sorted(data_lower, key=lambda x: x[3]), "}")
    return '\n'.join(res)
