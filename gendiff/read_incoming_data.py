#!/usr/bin/env python3
import json
import yaml
from yaml.loader import SafeLoader


def get_extension(path_to_data):
    if path_to_data[-4:] == ".yml" or path_to_data[-5:] == ".yaml":
        data_format = yaml
    elif path_to_data[-5:] == ".json":
        data_format = json
    else:
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
