#!/usr/bin/python3
"""Print sorted contents
"""


class MyList(list):
    """Print sorted list

    Arguments:
        list {[int]} -- [contains integers]
    """
    def print_sorted(self):
        print(sorted(self))
