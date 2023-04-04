#!/usr/bin/python3

def add_integer(a, b=98):
    """Addition function
    Args:
        a: can be integer or float
        b: can be integer or float
    Raise:
        TypeError: if a and b is not integer or float
    Return: the addition of a and b
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
