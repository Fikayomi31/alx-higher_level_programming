#!/usr/bin/python3

"""Defining a class"""


class Rectangle:
    """Representing a class rectangle"""

    def __init__(self, width=0, height=0):
        """Initializing the class rectangle
        Args:
            width: width of the rectangle
            height height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """getting the width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """setting the width attribute
        Raise:
            TypeError: if the width is not integer
            ValueError: if the width is < 0
        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """getting the height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setting the height attribute
        Raise:
            TypeError: if height is not integer
            ValueError: if height is < 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """return area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """return the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * (self.__width + self.__height))

    def __str__(self):
        """return a string representation of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ("")
        return "\n".join(["#" * self.__width] * self.__height)

    def __repr__(self):
        """return string representation of rectangle"""
        return "Rectangle {:d}, {:d}".format(self.__width, self.__height)
