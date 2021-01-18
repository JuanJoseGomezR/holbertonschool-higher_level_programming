#!/usr/bin/python3
"""function that writes an Object to a text file, using a JSON rep
"""


def save_to_json_file(my_obj, filename):
    """saves object to a file

    Arguments:
        my_obj {[type]} -- [description]
        filename {[type]} -- [description]
    """
    import json
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
