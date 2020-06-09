#!/usr/bin/python3
"""Base
"""


import json


class Base:
    """Base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """

        Args:
            id ([type], optional): [description]. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """list_dictionaries to JSON"""

        if list_dictionaries is None or list_dictionaries == []:
            return '[]'
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """list to JSON to file"""

        filename = cls.__name__ + '.json'
        with open(filename, 'w') as f:
            if list_objs is None:
                f.write(cls.to_json_string([]))
            else:
                l = [elem.to_dictionary() for elem in list_objs]
                f.write(cls.to_json_string(l))

    @staticmethod
    def from_json_string(json_string):
        """
        returns the list of the JSON string representation json_string:
        json_string is a string representing a list of dictionaries
        """

        if json_string is None or json_string == '':
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        returns an instance with all attributes already set
        """

        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        elif cls.__name__ == 'Square':
            dummy = cls(1)
        cls.update(dummy, **dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        that returns a list of instances
        """

        filename = cls.__name__ + '.json'
        if path.isfile(filename):
            with open(filename, 'r') as f:
                dictionary = cls.from_json_string(f.read())
            return [cls.create(**obj) for obj in dictionary]
        return []
