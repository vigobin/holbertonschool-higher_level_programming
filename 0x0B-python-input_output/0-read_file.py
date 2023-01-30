#!/usr/bin/python3
"""Read a file"""


def read_file(filename=""):
    """function that reads a text file (UTF8) and prints it to stdout.
    """
    s = filename
    with open(filename) as f:
        text = f.read()
        print(text, end="")
