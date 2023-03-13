#!/usr/bin/python3
"""Error code"""
import requests
from sys import argv


def errorcode():
    """Takes in a URL, sends a request to the URL
    and displays the body of the response"""
    response = requests.get(argv[1])
    try:
        if response.status_code > 400:
            print("Error code: {}".format(response.status_code))
        else:
            print(response.content.decode('utf-8'))
    except KeyError:
        pass

if __name__ == "__main__":
    errorcode()
