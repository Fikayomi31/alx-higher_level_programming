#!/usr/bin/python3
"""Scriptbthat take in a url, send a request to the url and
display value of the X-Requect-id variable found in the header
"""
import urllib.request
import sys

if __name__ == "__main__":

    url = sys.argv[1]

    """HTTP to GET request to the url and urlopen to open it"""
    response = urllib.request.Request(url)
    with urllib.request.urlopen(response) as respons:
        header = respons.info()["X-Request-Id"]
        print(header)
