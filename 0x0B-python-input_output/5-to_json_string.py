#!/usr/bin/python3
"""JSON rep of an objct
"""


def to_json_string(my_obj):
    """[summary]

    Arguments:
        my_obj {[type]} -- [description]
    """
    import json
    return json.dumps(my_obj)
