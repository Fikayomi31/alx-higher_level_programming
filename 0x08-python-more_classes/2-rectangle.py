#!/usr/bin/python3

"""Defining a class"""


class Rectangle:
    """Representing a class rectangle"""

    def __init__(self, width=0, height=0):
        """Initializing a class rectangle
        Args:
            width: the width of the rectangle
            height: the height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """getting the width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setting the width attribute
        Raise:
            TypeError: if the width is not integer
            ValueError: if the width is < 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError('width nust be >= 0')
        self.__width = value

    @property
    def height(self):
        """getting the height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """setting the height atteibute
        Raise:
            TypeError: if the height is not integer
            ValueError: if the height is < 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError('height nust be >= 0')
        self.__height = value

    def area(self):
        """return the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """return the perimeter"""
        if self.__width and self.__height == 0:
            return 0
        return ((self.__width * 2) + (self.__height * 2))
