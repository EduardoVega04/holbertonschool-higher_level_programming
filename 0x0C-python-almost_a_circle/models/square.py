#!/usr/bin/python3
"""Class Square that inherits from Rectangle. A square is a rectangle"""

from .rectangle import Rectangle


class Square(Rectangle):
    """Our class Square"""
    def __init__(self, size, x=0, y=0, id=None):
        """Construtor for our class"""
        super().__init__(size, size, x, y, id)
        self.size = size

    def __srt__(self):
        """User-friendly representation of the square"""
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(self.id,
                                                         self.x,
                                                         self.y,
                                                         self.width)