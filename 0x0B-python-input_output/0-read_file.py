#!/usr/bin/python3
"""This module define a text read function"""


def read_line(filename=""):
    """printing the content of the file"""
    with openi(filename, encoding="utf-8") as f:
        print(f.read(), end="")
