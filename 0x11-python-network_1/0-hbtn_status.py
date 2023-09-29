#!/usr/bin/python3

import urllib.request

if __name__ == "__main__":

    url = 'https://alx-intranet.hbtn.io/status'

    """HTTP GET request to the url"""
    response = urllib.request.Request(url)
    with urllib.request.urlopen(response) as respons:

        """read the content as bytes"""
        content = respons.read()

        """Decode the content to utf8"""
        content_utf8 = content.decode('utf-8')

        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(content_utf8))
