#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status"""
import urllib.request

if __name__ == "__main__":

    url = 'https://alx-intranet.hbtn.io/status'

    """HTTP to GET request to the url and urlopen to open it"""
    response = urllib.request.Request(url)
    with urllib.request.urlopen(response) as respons:

        """reading the content of the url http as bytes"""
        content = respons.read()

        """Decode the content of the url http to utf8"""
        content_utf8 = content.decode('utf-8')

        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(content_utf8))
