#!/usr/bin/python3
"""Base class for all other classes in this project
   it will manage id attribute in all future classes
   and to avoid duplicating the same code
"""


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
