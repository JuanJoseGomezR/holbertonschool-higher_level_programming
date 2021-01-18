#!/usr/bin/python3
"""[summary]
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """square inherited from rectangle

    Arguments:
        Rectangle {[type]} -- [description]
    """
    def __init__(self, size):
        """size

        Arguments:
            size {[type]} -- [description]
        """
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """string sqsuare"""
        return "[Square] " + "{}/{}".format(self.__size, self.__size)
