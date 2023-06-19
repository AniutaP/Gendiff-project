#!/usr/bin/env python3
from gendiff.generate import generate_diff, get_diff
from gendiff.parse_args import make_parse_args
from gendiff.read_files import read_file, find_file_type
from gendiff.formatter.stylish import stylish, make_stylish, stringify
from gendiff.formatter.format import get_format
from gendiff.formatter.plain import plain, make_plain, to_string
from gendiff.formatter.json import json_format


__all__ = ('generate_diff',
           'get_diff',
           'make_parse_args',
           'read_file',
           'stylish',
           'make_stylish',
           'stringify',
           'get_format',
           'plain',
           'make_plain',
           'to_string',
           'json_format',
           'find_file_type',
           )
