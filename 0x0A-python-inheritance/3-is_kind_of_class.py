#!/usr/bin/python3
"""object is an instance of, or if the object is an instance
"""


def is_kind_of_class(obj, a_class):
    """checks if the object is an instance of a class that inherited from

    Arguments:
        obj {[type]} -- [object we'll check]
        a_class {[type]} -- [class we'll check]

    Returns:
        [boolean] -- [True || false]
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
