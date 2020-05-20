#!/usr/bin/python3
"""Create a class Square"""


class Square:
    """Creates our beautiful square with some attributes"""
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """Function to retrieve size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter function for size"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >=0")
        else:
            self.__size = value

    def area(self):
        """Returns the area of a square"""
        return (self.__size * self.__size)
