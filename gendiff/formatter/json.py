#!/usr/bin/env python3
import json


def json_format(get_diff_list):
    return json.dumps(get_diff_list, indent=4)
