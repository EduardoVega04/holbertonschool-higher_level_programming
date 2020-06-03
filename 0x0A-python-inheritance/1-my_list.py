#!/usr/bin/python3
"""A class that inherits from list data type"""


class MyList(list):
    """The main class"""
    def print_sorted(self):
        """Inherits everything from class list (datatype)"""
        return (sorted(self))
