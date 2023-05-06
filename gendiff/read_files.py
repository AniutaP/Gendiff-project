#!/usr/bin/env python3
import json
import yaml
from yaml.loader import SafeLoader


def read_file(some_file):
    if some_file[-4:] == ".yml" or some_file[-5:] == ".yaml":
        return yaml.load(open(some_file), Loader=SafeLoader)
    if some_file[-5:] == ".json":
        return json.load(open(some_file))
