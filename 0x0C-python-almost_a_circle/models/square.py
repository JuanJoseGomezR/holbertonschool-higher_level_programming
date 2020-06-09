#!/usr/bin/python3
"""square
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """square class

    Args:
        Rectangle ([type]): [description]
    """
    def __init__(self, size, x=0, y=0, id=None):
        """initialize

        Args:
            size ([type]): [description]
            x (int, optional): [description]. Defaults to 0.
            y (int, optional): [description]. Defaults to 0.
            id ([type], optional): [description]. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """string
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y,
                                                 self.height)

    @property
    def size(self):
        """gets the size"""
        return self.height

    @size.setter
    def size(self, value):
        """sets size"""
        if type(value) != int:
            raise TypeError("width must be an integer")

        if value <= 0:
            raise ValueError("width must be > 0")

        self.width = value
        self.height = value

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
        """dictionary representation"""

        sque_dict = {}
        sque_dict['id'] = self.id
        sque_dict['size'] = self.width
        sque_dict['x'] = self.x
        sque_dict['y'] = self.y

        return sque_dict
