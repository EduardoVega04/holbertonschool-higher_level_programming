#!/usr/bin/python3
"""Creates a class Rectangle that defines a rectangle"""


class Rectangle:
    """New class Rectangle"""

    def __init__(self, width=0, height=0):
        """Constructor for the triangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter for the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for the width of the rectangle"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Getter for the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for the height of the rectangle"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Returns the area of the rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Returns the perimeter of the rectangle"""
        return (2 * (self.__width + self.__height))

    def __str__(self):
        """Prints the rectangle"""
        string = ""
        for a in range(self.__height):
            if a == self.__height - 1:
                string += self.__width * '#'
            else:
                string += self.__width * '#' + '\n'
        return string
