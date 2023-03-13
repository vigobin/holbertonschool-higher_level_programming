#!/usr/bin/python3
"""My GitHub!"""
import requests
from sys import argv
from requests.auth import HTTPBasicAuth


def git():
    """ takes your GitHub credentials (username and password)
    and uses the GitHub API to display your id"""
    url = 'https://api.github.com/user'
    username = argv[1]
    password = argv[2]

    data = requests.get(url, auth=(username, password))
    if data.status_code == requests.codes.ok:
        new_dict = data.json()
        print(new_dict['id'])
    else:
        print('None')


if __name__ == "__main__":
    git()
