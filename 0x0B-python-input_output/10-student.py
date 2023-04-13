#!/usr/bin/python3
"""Defining a class"""


class Student:
    """Representarion of a class student"""

    def __init__(self, first_name, last_name, age):
        """Initializing the class student
        Args:
            first_name: first name of the class
            last_name: last name of the class
            age: age of the class
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retriveing the representation of class student
        Args:
            attrs: a list of string (option) attribute to represent
            if the attrs = list and the loop of the attr = str
            it will return it attribute and value
        """
        if (type(attrs) == list and
                all(type(i) == str for i in attrs)):
            return {j: getattr(self, j) for j in attrs if hasattr(self, j)}
        return self.__dict__
