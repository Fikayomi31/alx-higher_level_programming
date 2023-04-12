#!/usr/bin/python3
"""This module return json representation of a string"""
import json


def to_json_string(my_obj):
    """return json of my_obj
    Arg:
        my_obj: an object to return
    """
    return json.dumps(my_obj)
