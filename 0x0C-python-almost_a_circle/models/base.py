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

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file"""
        objs = []
        filename = cls.__name__ + ".json"

        if not (list_objs is None):
            for i in list_objs:
                objs.append(cls.to_dictionary(i))

        with open(filename, "w") as file:
            file.write(cls.to_json_string(objs))
