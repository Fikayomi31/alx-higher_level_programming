#!/usr/bin/python3
"""Defining a class rectangle"""

from models.base import Base


class Rectangle(Base):
    """Representing a class rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializing the class rectangle
        Args:
            width: width of the rectangle
            height: height of the rectangle
            x: the x cordinator the rectangle
            y: the y cordinator of the rectangle
            id: the id of the rectangle which is an
                instance of class Base
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """return the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setting the width of the rectangle
        Args:
            value: value of the width
        Raise:
            TypeError: if the value is not an integer
            ValueError: if value is < 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """return the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setting the height of the rectangle
        Args:
            value: value of the height
        Raise:
            TypeError: if the height is not an integer
            ValueError: if the height is < 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """return x of the rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        """setting the value for x
        Args:
            value: value of x
        Raise:
            TyoeError: if x is not an integer
            ValueError: if x < 0
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x muat be >= 0")
        self.__x = value

    @property
    def y(self):
        """return the value for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """setting the value for y
        Args:
            value: value for y
        Raise:
            TypeError: if y is not an intege
            ValueError: if y < 0
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """return area of rectangle class"""
        return self.__width * self.__height
