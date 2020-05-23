#!/usr/bin/python3
"""
Prints out your name
"""


def say_my_name(first_name, last_name=""):
    """prints first and last name

    Arguments:
        first_name {[str]} -- [1st name]

    Keyword Arguments:
        last_name {str} -- [last name] (default: {""})

    Raises:
        TypeError: [must be a string]
        TypeError: [must be a string]
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
