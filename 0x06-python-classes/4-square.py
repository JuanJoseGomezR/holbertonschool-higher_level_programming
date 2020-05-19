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

    def size(self):
        """Retrieves itself"""
        return self.__size

    def size(self, value):
        """sets area of square"""
        if not type(value) == int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """area of the square"""
        return self.__size**2
