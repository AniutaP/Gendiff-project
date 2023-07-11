#!/usr/bin/env python3
from gendiff.read_files import read_file
from gendiff.formatter.format import get_format
from gendiff.difference import get_diff


def generate_diff(file1, file2, formatter='stylish'):
    file_data_1 = read_file(file1)
    file_data_2 = read_file(file2)
    data_diff = get_diff(file_data_1, file_data_2)
    return get_format(data_diff, formatter)
