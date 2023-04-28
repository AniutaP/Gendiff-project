#!/usr/bin/env python3
import json
import itertools


def generate_diff(first_file, second_file):
    file_path1_data = json.load(first_file)
    file_path2_data = json.load(second_file)
    data = []
    for key in file_path1_data:
        if key not in file_path2_data:
            data.append(f' - {key}: {file_path1_data[key]}')
        elif file_path1_data[key] == file_path2_data[key]:
            data.append(f'   {key}: {file_path1_data[key]}')
        elif file_path1_data[key] != file_path2_data[key]:
            data.append(f' - {key}: {file_path1_data[key]}')
            data.append(f' + {key}: {file_path2_data[key]}')
    for key in file_path2_data:
        if key not in file_path1_data:
            data.append(f' + {key}: {file_path2_data[key]}')
    result = "\n".join(sorted(data, key=lambda x: x[3]))
    print('{')
    print(result)
    print('}')
