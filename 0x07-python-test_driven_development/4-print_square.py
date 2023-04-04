#!/usr/bin/python3

"""function that prints a square with the character #"""


def print_square(size):
    """print # character
    Args:
        size: the size of the character to print
    Raise:
        TypeError: if the size is not an integer
        ValueError: if size is < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size == float:
        raise TypeError("size must be an integer")

    for i in range(size):
        for j in range(size):
            print('#', end='')
        print()
