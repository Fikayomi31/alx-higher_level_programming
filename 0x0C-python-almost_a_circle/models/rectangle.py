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
            id: the id of the rectangle
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
        """setting the width of the rectangle"""
        self.__width = value

    @property
    def height(self):
        """return the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setting the height of the rectangle"""
        self.__height = value

    @property
    def x(self):
        """return x of the rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        """setting the value for x"""
        self.__x = value

    @property
    def y(self):
        """return the value for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """setting the value for y"""
        self.__y = value
