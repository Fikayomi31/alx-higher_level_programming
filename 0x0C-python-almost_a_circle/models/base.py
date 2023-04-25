#!/usr/bin/python3
"""Defining a class base"""

import json
import csv
import os

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

    @staticmethod
    def to_json_string(list_dictionaries):
        """return json string representation of list_dictionary"""
        if not list_dictionaries or list_dictionaries == []:
            return "[]"
        if not isinstance(list_dictionaries, list):
            raise TypeError("list_dictionaries must be a list of dictionaries")
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """json string representationbof list_objs to a file"""
        filename = cls.__name__ + ".json"
        with open(filename, 'w') as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [j.to_dictionary() for j in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))
