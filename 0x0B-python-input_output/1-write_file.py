#!/usr/bin/python3
"""This module defines abfile-writing functions."""


def write_file(filename="", text=""):
    """We write a string to a UTF8 text file
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
