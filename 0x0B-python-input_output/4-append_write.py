#!/usr/bin/python3
"""append text
"""


def append_write(filename="", text=""):
    """append text to a file

    Keyword Arguments:
        filename {str} -- [description] (default: {""})
        text {str} -- [description] (default: {""})

    Returns:
        [type] -- [description]
    """
    with open(filename, 'a+') as file:
        return file.write(text)
