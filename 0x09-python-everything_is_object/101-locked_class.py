#!/usr/bin/ython3

class LockedClass:
    """the class prevent dynamic creation of attributes other
    than first_name
    """

    __slots__ = ['first_name']
