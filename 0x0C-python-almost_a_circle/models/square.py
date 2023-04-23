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

    def update(self, *args, **kwargs):
        """update argrument
        Args:
            args: attribute agrument
                -1st argument for id attribute
                -2nd argument for size attribute
                -3rd argument for x attribute
                -4th argument for y attribute
            kwargs:(dict) key and value argument to attribute
        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.size = arg
                elif a == 2:
                    self.x = arg
                elif a == 3:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """return the dictionary representation of a Rectangle"""
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
