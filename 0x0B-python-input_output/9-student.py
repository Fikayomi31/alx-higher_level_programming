#!/usr/bin/python3
"""Defining a class"""

class Student:
    """Representation of class student"""

    def __init__(self, first_name, last_name, age):
        """Initializing the class student
        Args:
            first_name: first name if the class
            last_name: last name of the class
            age: age of the class
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves the reoresentation of student"""
        return self.__dict__
