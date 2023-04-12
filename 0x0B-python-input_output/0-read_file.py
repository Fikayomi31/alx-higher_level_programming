#!/usr/bin/pyn3

"""read module"""
def read_line(filename=""):
    with open("filename", mode='r', encoding="utf-8") as f:
        print(f.read())
