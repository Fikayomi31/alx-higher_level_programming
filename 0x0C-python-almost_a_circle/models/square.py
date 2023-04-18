#!/usr/bin/python3
"""Definning a class which is inherits Rectangle class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Representing a square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializing the new square and it inherits the attribute of
        Rectangle
        Args:
            size: size of the square and inherit width and height
            x: x coordinate of the square, inherit x
            y: y coordinate of the square, inherit  y
            id: identity of the square, inherit id
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """str representation of the class square"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.width)

    @property
    def size(self):
        """getting the size of the square"""
        return self.width

    @size.setter
    def size(self, value):
        """setting the value of the square
        Args:
            value: value can either be width or height
        Raise:
            TypeError: if value is not  an integer
            ValueError: if value is < 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value
