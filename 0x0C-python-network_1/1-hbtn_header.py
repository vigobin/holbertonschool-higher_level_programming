#!/usr/bin/python3
"""Response header value #0 """
import urllib.request
from sys import argv


def response():
    """takes in a URL, sends a request to the URL and displays
    the value of the X-Request-Id"""
    with urllib.request.urlopen(argv[1]) as response:
        r = response.headers
        print(r['X-Request-Id'])


if __name__ == "__main__":
    response()
