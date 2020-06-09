#!/usr/bin/python3
"""rectangle
"""


from models.base import Base


class Rectangle(Base):
    """New rectangle

    Args:
        Base ([type]): [description]
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """[summary]

        Args:
            width ([type]): [description]
            height ([type]): [description]
            x (int, optional): [description]. Defaults to 0.
            y (int, optional): [description]. Defaults to 0.
            id ([type], optional): [description]. Defaults to None.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """get width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width"""
        if type(value) != int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        """get height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height"""
        if type(value) != int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        """get x"""
        return self.__y

    @x.setter
    def x(self, value):
        """Set x"""
        if type(value) != int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        """get y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Set y"""
        if type(value) != int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """AREA"""
        return self.width * self.height

    def display(self):
        """DISPLAY RECTANGLE"""
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            print(' ' * self.__x + '#' * self.__width)

    def __str__(self):
        """[Rectangle] (<id>) <x>/<y> - <width>/<height>"""
        return "[Rectangle] " + "({}) {}/{} - {}/{}".format(self.id,
                                                            self.x,
                                                            self.y,
                                                            self.width,
                                                            self.height)

    def update(self, *args, **kwargs):
        """Update funct"""
        if kwargs is not None:
            for key, value in kwargs.items():
                setattr(self, key, value)
        if args is not None:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[0]
                elif i == 1:
                    self.width = args[1]
                elif i == 2:
                    self.height = args[2]
                elif i == 3:
                    self.x = args[3]
                elif i == 4:
                    self.y = args[4]

    def to_dictionary(self):
        """DICTIONARY"""
        rect_dict = {}
        rect_dict['id'] = self.id
        rect_dict['width'] = self.__width
        rect_dict['height'] = self.__height
        rect_dict['x'] = self.__x
        rect_dict['y'] = self.__y

        return rect_dict
