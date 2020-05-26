#!/usr/bin/python3
"""Creates a class Rectangle that defines a rectangle"""


class Rectangle:
    """New class Rectangle"""

    number_of_instances = 0

    @staticmethod
    def increment():
        """Increments the instances"""
        Rectangle.number_of_instances += 1

    @staticmethod
    def decrement():
        """Decrements the instances."""
        Rectangle.number_of_instances -= 1

    def __init__(self, width=0, height=0):
        """Constructor for the triangle"""
        self.width = width
        self.height = height
        self.increment()

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
        if self.height == 0 or self.width == 0:
            return ("")
        w = "#" * self.width
        printed = w
        for i in range(self.height-1):
            printed += "\n" + w
        return (printed)

    def __repr__(self):
        """Return a string representation of the rectangle"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """This function deletes an instance(object) of Rectangle"""
        self.decrement()
        print("Bye rectangle...")
