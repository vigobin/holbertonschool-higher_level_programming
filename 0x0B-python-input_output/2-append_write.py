#!/usr/bin/python3
"""The append write function"""


def append_write(filename="", text=""):
    """function that appends a string at the end of a text file (UTF8)
    and returns the number of characters added.
    """
    with open(filename, "a") as f:
        return f.write(text)
