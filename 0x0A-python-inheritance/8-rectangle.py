#!/usr/bin/python3
"""[summary]
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """[summary]

    Arguments:
        BaseGeometry {[type]} -- [description]
    """
    def __init__(self, width, height):
        """[summary]

        Arguments:
            width {[type]} -- [description]
            height {[type]} -- [description]
        """
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
