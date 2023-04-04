#!/usr/bin/python3

"""Defining a class"""


class Rectangle:
    """Representing a class rectangle"""

    def __init__(self, width=0, height=0):
        """Initializing the class rectangle
        Args:
            width: width of the rectangle
            height: height of the rectangle
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
            TypeError: if width is not integer
            ValueError: if width is < 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getting the heigth attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """setting the heigth attribute
        Raise:
            TypeError: if heigth is not integer
            ValueError: if heigth is < 0
        """
        if not isinstance(value, int):
            raise TypeError("heigth must be an integer")
        if value < 0:
            raise ValueError("heigth must be >= 0")
        self.__height = value

    def area(self):
        """return area of rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """return perimeter of the rectangle"""
        if self.__width or self.__height == 0:
            return 0
        return ((self.__width * 2) + (self.__height))

    def __str__(self):
        """return the string representarion of the Rectangle
        represent the string with #
        """
        if self.__width == 0 or self.__height == 0:
            return ("")
        return "\n".join(["#" * self.width] * self.height)
