#!/usr/bin/python3
def remove_char_at(str, n):
    # Check if n is valid index
    if n < 0:
        return str
    return str[:n] + str[n+1:]
