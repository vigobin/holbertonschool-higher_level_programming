#!/usr/bin/python3
"""What's my status? #1"""
import requests
from sys import argv


def status():
    """fetches https://intranet.hbtn.io/status"""
    response = requests.get('https://intranet.hbtn.io/status')
    print('Body response:')
    print('\t- type: {}'.format(type(response.text)))
    print('\t- content: {}'.format(response.text))


if __name__ == "__main__":
    status()
