#!/usr/bin/python3
"""Script that make yojr Github credentials(username and password)
use github API to display id
"""
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    username = sys.
    token = sys.argv[2]
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])

    r = requests.get("https://api.github.com/user", auth=auth)
    print(r.json())
