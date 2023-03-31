#!/usr/bin/python3

"""Defining a class"""


class Square:
    """Representing a class square"""

    def __init__(self, size=0):
        """Initializing a square"""
        self.__size = size

    @property
    def size(self):
        "''Get the current size of square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setting the value of size
        Args:
            size: the size of the square
        Raise:
            TypeError: if size is not a integer
            ValueError: if size is less than 0
        """
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """Return area of the square"""
        return self.__size * self.__size
