#!/usr/bin/python3
"""This module create an object from a json file"""
import json


def load_from_json_file(filename):
    """create an object from a json file
    Args:
        filename: the file to create object from
    """
    with open(filename, 'r') as f:
        return json.load(f)
