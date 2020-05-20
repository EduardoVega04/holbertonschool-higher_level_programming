#!/usr/bin/python3
"""Create a Square class"""


class Square:
    """Creates our beautiful square with it's amazing attributes"""
    def __init__(self, size=0):
        """Initializes square"""
        self.__size = size

    @property
    def size(self):
        """Retrieves the size of the square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Sets the size for our square, handling errors"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Returns the area of the square"""
        return (self.__size ** 2)

    def my_print(self):
        """Prints to stdout our square, of an empty line if it's size is 0"""
        vert = self.__size
        horiz = self.__size

        if self.__size == 0:
            print()
        else:
            for i in range(vert):
                for j in range(horiz):
                    print("#", end="")
