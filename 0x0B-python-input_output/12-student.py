#!/usr/bin/python3
"""Create class Student, retrieve a dictionary representation of an instance"""


class Student:
    """Our class Student"""
    def __init__(self, first_name, last_name, age):
        """Initializes an instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns dictionary representation of an instance"""
        dic = {}
        if attrs is None:
            return self.__dict__
        for i in attrs:
            if hasattr(self, i):
                dic[i] = getattr(self, i)
        return dic
