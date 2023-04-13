#!/usr/bin/python3
"""This module define a pascal triangle"""

def pascal_triangle(n):
    """function to a list of integer
    representing pascal triangle
    Args:
        n: the integer
    Return: an empty list if n <= 0 or
            a list of lists of integer
    """
    if n <= 0:
        return ""
    for i in range(n):
        print(" "*(n - 1), end='')
        print(' '.join(map(str, str(11 ** i))))
