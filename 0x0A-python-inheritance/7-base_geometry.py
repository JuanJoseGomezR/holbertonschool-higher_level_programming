#!/usr/bin/python3
"""[summary]
"""

class BaseGeometry:
    """new class
    """
    def area(self):
        """raises exception or not
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """VALIDATES

        Arguments:
            name {[type]} -- [description]
            value {[type]} -- [description]
        """
        if type(value) is not int:
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
