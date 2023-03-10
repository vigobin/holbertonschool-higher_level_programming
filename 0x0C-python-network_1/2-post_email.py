#!/usr/bin/python3
"""POST an email #0"""
from urllib import request, parse
from sys import argv


def post():
    """takes in a URL and an email, sends a POST request to the passed UR
      with the email as a parameter, """
    data = parse.urlencode({'email': argv[2]})
    data = data.encode()
    email = request.Request(argv[1], data)
    with request.urlopen(email) as response:
        r = response.read()
        print(r.decode('utf-8'))


if __name__ == "__main__":
    post()
