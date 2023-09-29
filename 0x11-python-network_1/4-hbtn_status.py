#!/usr/bin/python3
"""Fetch https://alx-intranet.hbtn.io/ststus with requests package
"""
import requests

if __name__ == "__main__":

    url = "https://alx-intranet.hbtn.io/status"
    req = requests.get(url)
    response = req.text
    print("Body response:")
    print("\t- type: {}".format(type(response)))
    print("\t- content: {}".format(response))
