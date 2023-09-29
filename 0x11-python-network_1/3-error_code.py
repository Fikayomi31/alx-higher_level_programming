#!/usr/bin/python3
"""Script that takes in a url, send a request to the url and display
the body of the response
"""
import sys
import urllib.request
import urllib.error

if __name__ == "__main__":

    url = sys.argv[1]
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as response:
            rep = response.read().decode('ascii')
            print(rep)
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
