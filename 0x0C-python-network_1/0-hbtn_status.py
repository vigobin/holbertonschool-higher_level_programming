#!/usr/bin/python3
"""What's my status? #0"""
import urllib.request


def fetch:
"""Python script that fetches https://intranet.hbtn.io/status"""
    with urllib.request.urlopen(https://intranet.hbtn.io/status) as response:
        html = response.read()
        print(html)
