#!/usr/bin/env python3
import json
import yaml
from yaml.loader import SafeLoader
import pathlib


def get_extension(path_to_data):
    formats = {'.yml': yaml, '.yaml': yaml, '.json': json}
    format = pathlib.PurePath(path_to_data).suffix
    data_format = formats[format]
    if not data_format:
        raise ValueError('Unknown format file')
    return data_format


def parse_format(path_to_data, file):
    extension = get_extension(path_to_data)
    if extension == yaml:
        return yaml.load(file, Loader=SafeLoader)
    if extension == json:
        return json.load(file)


def read_data(path_to_data):
    with open(path_to_data) as file:
        return parse_format(path_to_data, file)
