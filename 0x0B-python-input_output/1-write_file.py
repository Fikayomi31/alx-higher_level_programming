#!/usr/bin/python3
"""The module is a function that write text file"""


def write_file(filename="", text=""):
    """write strings to a utf-8 text file"""
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
