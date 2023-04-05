#!/usr/bin/ython3
"""defining a class"""


class LockedClass:
    """the class prevent dynamic creation of attributes other
    than first_name
    """

    __slots__ = ['first_name']
