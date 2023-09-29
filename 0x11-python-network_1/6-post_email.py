#!/usr/bin/python3
"""Takes a url and an email, send a post request to passed url with
the email as aparameter and finallh display bodgbof response
"""

import sys
import requests

if __name__ == "__main__":

    url = sys.argv[1]
    data = {'email': sys.argv[2]}

    r = requests.post(url, data)
    response = r.text
    print(response)
