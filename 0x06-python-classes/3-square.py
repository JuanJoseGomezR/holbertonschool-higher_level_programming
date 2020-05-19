#!/usr/bin/python3
"""define square"""


class Square:
    """Initialize"""
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        """attribute"""
        self.__size = size
    def area(self):
        """area of the square"""
        return self.__size**2
