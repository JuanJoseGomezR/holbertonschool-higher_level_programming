#!/usr/bin/python3
"""adds all arguments to a Python list, and then save them
"""


def load_from_json_file(filename):
    """add arguments and save them in a file

    Arguments:
        filename {[type]} -- [description]

    Returns:
        [type] -- [description]
    """
    import json
    with open(filename, 'r') as s:
        return json.load(s)
