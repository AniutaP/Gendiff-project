#!/usr/bin/env python3
import json
import yaml
from yaml.loader import SafeLoader


def read_file(some_file):
    if some_file[-4:] == ".yml" or some_file[-5:] == ".yaml":
        file_name = yaml
    elif some_file[-5:] == ".json":
        file_name = json
    else:
        raise ValueError('Unknown format file')

    file_data = open(some_file)
    return load_file_type(file_name, file_data)


def load_file_type(file_name, file_data):
    if file_name == yaml:
        return yaml.load(file_data, Loader=SafeLoader)
    if file_name == json:
        return json.load(file_data)
