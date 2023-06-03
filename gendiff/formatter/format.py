#!/usr/bin/env python3
from gendiff.formatter.stylish import stylish
from gendiff.formatter.plain import plain


def get_format(data_diff, formatter):
    if formatter == 'stylish':
        return stylish(data_diff)
    if formatter == 'plain':
        return plain(data_diff)
