#!/usr/bin/python3
""" Module for rectangle class """


class Rectangle:
    """  Class Rectangle that defines a rectangle """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ Getter for property width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter for property width """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Getter for property heigth """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter for property heigth """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Method that returns the rectangle area """
        return self.__width * self.__height

    def perimeter(self):
        """ Method that returns the rectangle perimeter """
        if self.__width == 0 or self.__height == 0:
            return 0
        return self.__width * 2 + self.__height * 2

    def __str__(self):
        """
        Method that returns a string with  the
        rectangle represented with the character #
        """
        string = ""
        if self.__width != 0 and self.__height != 0:
            for h in range(self.__height):
                string += self.__width * str(self.print_symbol) + "\n"
            string = string[:-1]
        return string

    def __repr__(self):
        """
        Method that returns a string representation of the rectangle
        to be able to recreate a new instance by using eval()
        """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """
        Method that prints a message when an
        instance of Rectangle is deleted
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Static method that returns the biggest
        rectangle based on the area
        """
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.area() > rect_1.area():
            return rect_2
        else:
            return rect_1
