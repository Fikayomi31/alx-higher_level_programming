#!/usr/bin/python3

"""Defining a class"""


class Square:
    """Representing a class square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initializing a new square
        Args:
            size: size of the square
            position: the position of the square
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Set the current size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """property of position of square"""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square
        Args:
            Value: value as two tuple
        Raise:
            TypeError: if value != a tuple of 2 integer <0
        """
        if not (isinstance(value, tuple) or
            len(value) != 2 or
            not all(isinstance(num, int) for num in value) or
            not all(num >= 0 for num in value)):
            raise TypeError("position must be tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Get the area of square
        Return: square of size
        """
        return self.__size * self.__size

    def my_print(self):
        """Print square with # character"""
        if self.__size == 0:
            print()
            return
        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print()
