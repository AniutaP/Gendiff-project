#!/usr/bin/env python3
from gendiff.read_incoming_data import read_data
from gendiff.formatter.format import get_format
from gendiff.difference import get_diff


def generate_diff(path1, path2, formatter='stylish'):
    entry_data1 = read_data(path1)
    entry_data2 = read_data(path2)
    data_diff = get_diff(entry_data1, entry_data2)
    return get_format(data_diff, formatter)
