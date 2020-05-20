#!/usr/bin/python3
"""Create a class Square"""


class Square:
    """Create a class Square with safe input (try/except)"""
    def __init__(self, size=0):
        """Init method with private field size"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
