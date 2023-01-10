#!/usr/bin/python3
"""This a module that define JSON file-writing function."""
import json


def save_to_json_file(my_obj, filename):
    """Write an object to a text using JSON representation.
    """
    with open(filename, "w") as f:
        json.dump(my_obj, f)
