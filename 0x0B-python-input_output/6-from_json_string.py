#!/usr/bin/python3
"""RETURNS OBJECT IN JSON
"""


def from_json_string(my_str):
    """str representend in json stirng

    Arguments:
        my_str {[type]} -- [description]
    """
    import json
    return json.loads(my_str)
