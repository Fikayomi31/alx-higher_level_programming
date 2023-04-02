#!/usr/bin/python3

"""function to print first name and last name"""


def say_my_name(first_name, last_name=""):
    """module for first and last name
    Args:
        first_name: to take the string first name
        last_name: to take the string last name
    raise:
        TypeError: if first and last name are not string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("{} {}".format(first_name, last_name))
