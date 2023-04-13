#!/usr/bin/python3
"""Definig the class"""


class Student:
    """Representation of the class student"""

    def __init__(self, first_name, last_name, age):
        """Initializing the class student
        Args:
            first_name: public instance attribute for first name
            last_name: public instance attribute for last name
            age: public instance attribute for age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve a dictionary representation of a class
        student
        Args:
            attrs: attribute contain in a list of string or list
        """
        if (type(attrs) == list and
                all(type(i) == str for i in attrs)):
            return {j: getattr(self, j) for j in attrs if hasattr(self, j)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attribute of the class student
        """
        for i, j in json.items():
            setattr(self, i, j)
