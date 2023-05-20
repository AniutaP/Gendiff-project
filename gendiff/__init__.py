#!/usr/bin/env python3
from gendiff.generate import generate_diff
from gendiff.parse_args import make_parse_args
from gendiff.read_files import read_file
from gendiff.formatter.stylish import stylish, stringify
from gendiff.formatter.format import get_format


__all__ = ('generate_diff',
           'get_diff',
           'make_parse_args',
           'read_file',
           'stylish',
           'stringify',
           'get_format'
           )
