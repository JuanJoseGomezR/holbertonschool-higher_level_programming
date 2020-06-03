#!/usr/bin/python3
"""Writes a string to a txt file
"""


def write_file(filename="", text=""):
    """writes in a file

    Keyword Arguments:
        filename {str} -- [description] (default: {""})
        text {str} -- [description] (default: {""})

    Returns:
        [type] -- [description]
    """
    with open(filename, 'w') as file:
        return file.write(text)
