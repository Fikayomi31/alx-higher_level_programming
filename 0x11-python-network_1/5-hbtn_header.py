#!/usr/bin/python3
"""Takes in url, sends a request to the url and display the value of
X-Request-Id in the response header
"""

import requests
import sys

if __name__ == "__main__":

    url = sys.argv[1]

    response = requests.get(url)
    result = response.headers.get('X-Request-Id')
    print(result)
