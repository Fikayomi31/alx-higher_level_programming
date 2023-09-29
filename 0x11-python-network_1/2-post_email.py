#!/usr/bin/python3
"""Script to takes in a url and email send a post request to url
with rhe email as a parameter and display the body of the reponse
"""
import sys
import urllib.parse
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]
    value = {'email': sys.argv[2]}

    data = urllib.parse.urlencode(value)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        email_output = response.read().decode('utf-8')
        print(email_output)
