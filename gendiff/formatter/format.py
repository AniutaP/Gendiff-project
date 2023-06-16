#!/usr/bin/env python3
from gendiff.formatter.stylish import stylish
from gendiff.formatter.plain import plain
from gendiff.formatter.json import json_format


def get_format(data_diff, formatter):
    if formatter == 'stylish':
        return stylish(data_diff)
    if formatter == 'plain':
        return plain(data_diff)
    if formatter == 'json':
        return json_format(data_diff)
    raise ValueError('Unknown format name')
