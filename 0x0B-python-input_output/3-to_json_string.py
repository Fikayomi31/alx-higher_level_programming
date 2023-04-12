#!/usr/bin/python3
"""This module return json representation of a string"""
import json


def to_json_string(my_obj):
    """print json of my_obj"""
    return json.dumps(my_obj)
