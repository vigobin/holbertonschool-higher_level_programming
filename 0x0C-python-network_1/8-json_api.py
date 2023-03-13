#!/usr/bin/python3
"""Search API"""
import requests
from sys import argv


def search():
    """akes in a letter and sends a POST request to the url
    with the letter as a parameter."""
    url = 'http://0.0.0.0:5000/search_user'
    if len(argv) > 1:
        q = argv[1]
    else:
        q = ""

    values = {'q': q}

    r = requests.post(url, data=values)
    try:
        data = r.json()
        if len(data) == 0:
            print("No result")
        else:
            print("[{}] {}".format(data['id'], data['name']))
    except ValueError as e:
        print('Not a valid JSON')


if __name__ == "__main__":
    search()
