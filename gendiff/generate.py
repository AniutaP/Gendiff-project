#!/usr/bin/env python3
from gendiff.read_incoming_data import read_data
from gendiff.formatter.format import get_format
from gendiff.difference import get_diff


def generate_diff(data1, data2, formatter='stylish'):
    received_data1 = read_data(data1)
    received_data2 = read_data(data2)
    data_diff = get_diff(received_data1, received_data2)
    return get_format(data_diff, formatter)
