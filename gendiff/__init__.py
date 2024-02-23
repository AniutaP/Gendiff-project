#!/usr/bin/env python3
from gendiff.generate import generate_diff
from gendiff.difference import get_diff
from gendiff.parse_args import make_parse_args
from gendiff.read_incoming_data import read_data, parse_format, get_extension
from gendiff.formatter.stylish import (
    stylish, make_stylish, stringify, make_indent
)
from gendiff.formatter.format import get_format
from gendiff.formatter.plain import plain, get_plain, make_string
from gendiff.formatter.json import json_format


__all__ = ('generate_diff',
           'get_diff',
           'make_parse_args',
           'read_data',
           'get_extension',
           'parse_format',
           'stylish',
           'make_stylish',
           'stringify',
           'make_indent',
           'get_format',
           'plain',
           'get_plain',
           'make_string',
           'json_format',
           )
