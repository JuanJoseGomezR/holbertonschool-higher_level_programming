#!/usr/bin/python3
"""Check if it's an instance of the class
"""


def is_same_class(obj, a_class):
    """chech instance

    Arguments:
        obj {[]} -- [object]
        a_class {[a_class]} -- [class to check]

    Returns:
        [boolean] -- [True || False]
    """
    if type(obj) == a_class:
        return True
    else:
        return False
