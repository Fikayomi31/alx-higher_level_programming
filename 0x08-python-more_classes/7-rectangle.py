#!/usr/bin/python3
"""Defining a class Rectangle"""


class Rectangle:
    """Representing a class rectangle"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initializing the class rectangle
        Args:
            width: width of the rectangke
            height: height of the rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Retrieve the width of the class"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setting the value of the width
        Args:
            value: value of the width
        Raise:
            TypeError: if width is not an integer
            ValueError: if width is not >= 0
        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """Retrieve the height of the class"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setting the value of the height
        Args:
            value: value of the height
        Raise:
            TypeError: if height is not an integer
            ValueError: if height is not >= 0
        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """return the area of the class rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """return the perimeter of the rectangle"""
        if self.__width or self.__height == 0:
            return 0
        return (2 * (self.__width + self.__height))

    def __str__(self):
        """print rectangle with character"""
        if self.__width or self.__height == 0:
            return ""
        """printing out the #"""
        rec = []
        for i in range(self.__height):
            [rec.append(str(self.print_symbol)) for j in range(self.__width)]
            if i != self.__height - 1:
                rec.append("\n")
        return ("".join(rec))

    def _repr__(self):
        """return string representation of the rectangle"""
        return "Rectangle({:s}, {:s})".format(str(self.__width),
                                              str(self.__height))

    def __del__(self):
        """print a del message for the class deleted"""
        Rectangle.number_of_instances -= 1

        print("Bye rectangle...")
