#!/usr/bin/python3
"""This module define a file-appending function."""


def append_write(filename="", text=""):
    """Append a string to the end of UTF8 text file.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return  f.write(text)
