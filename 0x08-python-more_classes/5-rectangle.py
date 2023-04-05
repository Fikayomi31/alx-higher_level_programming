#!/usr/bin/python3

"""Defining a class"""


class Rectangle:
    """Representation of the class rectangle"""

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
        """retrieve the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setting the value of the width
        Args:
            value: value of the width
        Raise:
            TypeError: if width is not an integer
            ValueError: if width is < 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrieve the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setting the value of the height
        Args:
            Value: value of the height
        Raise:
            TypeError: if the height is not an integer
            ValueError: if height is < 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """return the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """return the perimeter of the rectangle"""
        if self.__width or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return printable representation of Rectangle"""
        if self.__width or self.__height == 0:
            return ("")
        return "\n".join(["#" * self.__width] * seld.__height)

    def __repr__(self):
        """the string representation of Rectangle"""
        return "Rectangle({:s}, {:s})".format(str(self.__width),
                                              str(self.__height))

    def __del__(self):
        """deleting the representation of Rectangle"""
        print("Bye rectangle...")
