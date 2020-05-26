#!/usr/bin/python3
"""

    Raises:
        TypeError: [description]
        ValueError: [description]
        TypeError: [description]
        ValueError: [description]
        TypeError: [description]
        ValueError: [description]
        TypeError: [description]
        ValueError: [description]

    Returns:
        [type] -- [description]
"""


class Rectangle:
    print_symbol = '#'
    number_of_instances = 0
    """Real Rectangle."""
    def __init__(self, width=0, height=0):
        """Init"""
        if type(width) != int:
            raise TypeError('width must be an integer')
        if width < 0:
            raise ValueError('width must be >= 0')
        if type(height) != int:
            raise TypeError('height must be an integer')
        if height < 0:
            raise ValueError('height must be >= 0')
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width"""
        if type(value) != int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height"""
        if type(value) != int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """area"""
        return self.__width * self.__height

    def perimeter(self):
        """perimeter"""
        if self.__width == 0 or self.height == 0:
            return 0
        return (2 * self.__width) + (2 * self.__height)

    def __str__(self):
        """rectangle of #'s"""
        str = ""
        if self.__width == 0 or self.__height == 0:
            return str
        strsym = "{}".format(Rectangle.print_symbol)
        if self.print_symbol:
            strsym = "{}".format(self.print_symbol)
        for a in range(self.__height):
            for b in range(self.width):
                str += strsym
            if a != self.height - 1:
                str += '\n'
        return str

    def __repr__(self):
        """eval'ible representation of Rectangle"""

        w = str(self.__width)
        h = str(self.__height)
        return 'Rectangle(' + w + ', ' + h + ')'

    def __del__(self):
        """del"""
        print('Bye rectangle...')
        Rectangle.number_of_instances -= 1
