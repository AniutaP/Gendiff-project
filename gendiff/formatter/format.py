#!/usr/bin/env python3
from gendiff.formatter.stylish import stylish


def get_format(data_diff, formatter):
    if formatter == 'stylish':
        return stylish(data_diff)
