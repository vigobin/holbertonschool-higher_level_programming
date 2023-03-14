#!/usr/bin/python3
"""Response header value"""
from sys import argv
import requests


def response():
    """takes in a URL, sends a request to the URL and displays the
    value of the variable X-Request-Id"""
    response = requests.get(argv[1])
    r = response.headers
    print(r.get('X-Request-Id'))


if __name__ == '__main__':
    response()
