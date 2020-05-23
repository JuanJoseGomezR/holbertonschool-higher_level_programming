#!/usr/bin/python3
"""
Prints square #
"""


def print_square(size):
    """[Print a square made of #]

    Arguments:
        size {[int]} -- [size of square]

    Raises:
        TypeError: [must be an int]
        ValueError: [must be >= 0]
        TypeError: [must be an int]
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    for row in range(0, size):
        for column in range(0, size):
            print("#", end="")
        print()
