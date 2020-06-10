#!/usr/bin/python3
"""Class Square that inherits from Rectangle. A square is a rectangle"""

from .rectangle import Rectangle


class Square(Rectangle):
    """Our class Square"""
    def __init__(self, size, x=0, y=0, id=None):
        """Construtor for our class"""
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """User-friendly representation of the square"""
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(self.id,
                                                         self.x,
                                                         self.y,
                                                         self.width)

    @property
    def size(self):
        """Getter for the size of the Square"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for the size of the Square"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.width = value
            self.height = self.width
