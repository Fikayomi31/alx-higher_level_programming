#!/usr/bin/python3
"""Defining the class square"""


class Square:
    """Representation of the class"""

    def __init__(self, size=0, position=(0, 0)):
        """ Initializing the class"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Return the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setting the value for the size
        Args:
            value: value for the size
        Raise:
            TypeError: if size not an integer
            ValueError: if size is < 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__posiition

    @position.setter
    def position(self, value):
        """Setting the value for the position
        Args:
            value: value for the position
        Raise:
            TypeError: if position is not tuple or interger
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integer")
        if not all(isinstance(num, int) and num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integer")
        self.__position = value

    def area(self):
        """Return current square root"""
        return self.__size * self.__size

    def my_print(self):
        """Print the square with the # character."""
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")

    def __str__(self):
        """Define the print() representation of a Square."""
        if self.__size != 0:
            [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            if i != self.__size - 1:
                print("")
        return ("")
