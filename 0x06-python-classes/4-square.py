#!/usr/bin/python3

"""Defining a class"""


class Square:
    """Representing a class square"""

    def __init__(self, size=0):
        """Initializing a square
        Args:
            size: the size of the square
        Raise:
            TypeError: if size is not a integer
            ValueError: if size is less than 0
        """
        self.__size = size

    @property
    def size(self):
        "''Get the current size of square"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be integer')
        elif value < 0:
            raise ValueError('size mustbbe >= 0')
        self.__size = value

    def area(self):
        """Return area of the square"""
        return self.__size * self.__size
