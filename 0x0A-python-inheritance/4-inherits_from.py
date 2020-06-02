#!/usr/bin/python3
""" instance of a class that inherited (directly or indirectly)
"""


def inherits_from(obj, a_class):
    """[summary]

    Arguments:
        obj {[type]} -- [description]
        a_class {[type]} -- [description]
    """
    if type(obj) != a_class or not isinstance(obj, a_class):
        return True
    else:
        return False
