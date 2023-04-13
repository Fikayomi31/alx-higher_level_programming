#!/usr/bin/python3
"""Defining a class"""


class MyList(list):
    """subclass of list class"""

    def __init__(self):
        """Initializing the subclass"""
        super().__init__()

    def print_sorted(self):
        print(sorted(self))
