#!/usr/bin/python3
"""Defining a class base"""


class Base:
    """Representing the class base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializing the class base"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects