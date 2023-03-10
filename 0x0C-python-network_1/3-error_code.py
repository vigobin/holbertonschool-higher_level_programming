#!/usr/bin/python3
"""Error code task3"""
from urllib import request, error
from sys import argv


def error():
    try:
        with request.urlopen(argv[1]) as response:
            r = response.read()
            print(r.decode('utf-8'))
    except error.HTTPError as error:
        print("Error code: {}".format(error.code))


if __name__ == "__main__":
    error()
