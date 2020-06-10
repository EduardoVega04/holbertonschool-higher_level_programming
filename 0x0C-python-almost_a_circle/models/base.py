#!/usr/bin/python3
"""Base class for all other classes in this project
   it will manage id attribute in all future classes
   and to avoid duplicating the same code
"""

import json


class Base:
    """Our base class for this project"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor for this class"""
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            list_dictionaries = []
        return (json.dumps(list_dictionaries))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file"""
        objs = []
        filename = cls.__name__ + ".json"

        if (list_objs is not None):
            for i in list_objs:
                objs.append(cls.to_dictionary(i))

        with open(filename, "w") as f:
            f.write(cls.to_json_string(objs))

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all the attributes already set"""
        if cls.__name__ is 'Rectangle':
            dummy = cls(1, 1)
        elif cls.__name__ is 'Square':
            dummy = cls(1)
        dummy.update(**dictionary)
        return (dummy)

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances of type caller class from a file"""
        filename = cls.__name__ + ".json"
        l = []
        try:
            with open(filename, 'r') as f:
                l = cls.from_json_string(f.read())
            for i, e in enumerate(l):
                l[i] = cls.create(**l[i])
        except:
            pass
        return l
