#!/usr/bin/python3

"""Defining a class"""


class Square:
    """Representing class square"""

    def __init__(self, size=0):
        """Initializing a class square
        Args:
            size: size of the class square
        Raise:
            ValueError: if size is less than zero
            TypeError: if size is not integer
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """Area of the square
        Return: Square of the siz
        """
        return self.__size * self.__size
