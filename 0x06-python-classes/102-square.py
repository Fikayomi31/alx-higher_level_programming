#!/usr/bin/python3
"""Defining the class"""


class Square:
    """Representation of the square"""

    def __init__(self, size=0):
        """initializiation of the square"""
        self.size = size

    @property
    def size(self):
        """Return the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setting the value for the size
        Args:
            value: value of the square
        Raise:
            TypeError: if size is not a number
            ValueError: if size is < 0
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return area of the square"""
        return self.__size * self.__size

    def __eq__(self, other):
        """for == comparision"""
        return self.area() == other.area()

    def __lt__(self, other):
        """for < comparision"""
        return self.area() < other.area()

    def __le__(self, other):
        """for <= comparision"""
        return self.area() <= other.area()

    def __gt__(self, other):
        """for > comparision"""
        return self.area() > other.area()

    def __ge__(self, other):
        """for >= comparision"""
        return self.area() >= other.area()

    def __ne__(self, other):
        """for !n comparision"""
        return self.area() != other.area()
