#!/usr/bin/python3

"""Defining a class"""


class Rectangle:
    """Representing a class rectangle"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initializing a class rectangle
        Args:
            width: width of the rectangle
            height: height of the rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Retrieve the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setting the width
        Args:
            value: value of the width
        Raise:
            TypeError: if the width is not an intege
            ValueError: if the width is < 0
        """
        self.__width = value

    @property
    def height(self):
        """Retrieve the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setting the value of the height
        Args:
            value: value of the height
        Raise:
            TypeError: if the height is not an integer
            ValueError: if the height is < 0
        """
        self.__height = value

    def area(self):
        """return the area of rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """return the perimeter of the rectangle"""
        if self._width or self.__height == 0:
            return 0
        return (2 * (self.__width + self.__height))

    def __str__(self):
        """print the representation of the class rectangle"""
        if self.__width or self.__height == 0:
            return ("")
        return "\n".join(["#" * self.__width] * self.__height)

    def _repr__(self):
        """return string representation of the rectangle"""
        return "Rectangle({:s}, {:s})".format(str(self.__width),
                                              str(self.__height))

    def __del__(self):
        """print a del message for the class deleted"""
        print("Bye Rectangle...")
        Rectangle.number_of_instances -= 1
