#!/usr/bin/python3
"""Defining module that read file in a function"""


def read_file(filename=""):
    """print the content of the file"""
    with open(filename, 'r', encoding="utf-8") as f:
        print(f.read(), end="")
