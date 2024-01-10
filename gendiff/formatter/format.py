#!/usr/bin/env python3
from gendiff.formatter.stylish import stylish
from gendiff.formatter.plain import plain
from gendiff.formatter.json import json_format


def get_format(data_diff, formatter):
    available_formats = {'stylish': stylish(data_diff),
                         'plain': plain(data_diff),
                         'json': json_format(data_diff)
                         }
    if formatter in available_formats:
        return available_formats[formatter]
    raise ValueError('Unknown format name')
