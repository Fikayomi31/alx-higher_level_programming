#!/usr/bin/python3
"""This module returns an object represented by a
json string
"""
import json


def from_json_string(my_str):
    """Return an object from json string
    Args:
        my_str: the string
    """
    return json.loads(my_str)
