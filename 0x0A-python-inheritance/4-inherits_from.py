#!/usr/bin/python3
""" instance of a class that inherited (directly or indirectly)
"""


def inherits_from(obj, a_class):
    """[summary]

    Arguments:
        obj {[type]} -- [description]
        a_class {[type]} -- [description]

    Returns:
        [type] -- [description]
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
