#!/usr/bin/python3
"""This module define a JSON file reading function."""
import json


def load_from_json(filename):
    """Create a python object from a JSON file."""
    withbopen(filename) as f:
        return json.load(f)
