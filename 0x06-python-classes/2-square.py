#!/usr/bin/python3

"""Defining a class"""


class Square:
    """Represent a class"""

    def __init__(self, size=0):
        """Initializing the square class
        Args:
            size: represent the size of square
        raise:
            TypeError: if size is not integer
            ValueError: if size is > 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
