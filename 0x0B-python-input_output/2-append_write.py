#!/usr/bin/python3
"""This module define a text file that appends"""


def append_write(filename="", text=""):
    """write a string to utf-8 that append"""
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
