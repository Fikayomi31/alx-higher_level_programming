#!/usr/bin/python3
"""This module write an objec to a text file using
json representation
"""
import json


def save_to_json_file(my_obj, filename):
    """return a json that write an object
    Args:
        my_obj: the string
        filename: file name
    """
    with open(filename, 'w') as f:
        string = json.dumps(my_obj)
        f.write(string)
