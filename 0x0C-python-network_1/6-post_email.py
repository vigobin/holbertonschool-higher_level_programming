#!/usr/bin/python3
"""POST an email #1"""
import requests
from sys import argv


def post1():
    """Takes in a URL and an email address, sends a POST request to the passed
    URL with the email as a parameter,
    and finally displays the body of the response."""
    response = requests.post(argv[1])
    print(response)


if __name__ == '__main__':
    post1()
