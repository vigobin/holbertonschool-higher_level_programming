#!/usr/bin/python3
"""Error code task3"""
from urllib import request, error
from sys import argv
import urllib


def error():
    url = argv[1]
    req = request.Request(url)
    try:
        with request.urlopen(req) as response:
            r = response.read()
            print(r.decode('utf-8'))
    except urllib.error.HTTPError as err:
        print("Error code: {}".format(err.code))


if __name__ == "__main__":
    error()
