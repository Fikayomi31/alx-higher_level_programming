#!/usr/bin/python3
"""This module return the dictionary description"""


def class_to_json(obj):
    """return all the attribute of the class object
    Args:
        obj: the class
    """
    return obj.__dict__
