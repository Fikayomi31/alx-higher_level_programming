#!/usr/bin/python3

"""Defining a class"""


class Rectangle:
    """Representing the class rectangle"""

    def __init__(self, width=0, height=0):
        """Initializing the class rectangle
        Args:
            width: width of the rectangle
            height: height of the rectangle
        Raise:
            TypeError: if the width is not integer
            ValueError: if the width is < than 0
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """retrieves the width attributes"""
        return self.__width

    @width.setter
    def width(self, value):
        """setting the width attribute"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """reterive the height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
