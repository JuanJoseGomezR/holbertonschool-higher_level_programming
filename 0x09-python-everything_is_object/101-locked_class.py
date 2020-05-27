#!/usr/bin/python3
"""
defines locked class
"""


class LockedClass:
    """prev form creating new
    """
    __slots__ = ['first_name']

    def __init__(self, first_n=""):
        self.first_name = first_n
