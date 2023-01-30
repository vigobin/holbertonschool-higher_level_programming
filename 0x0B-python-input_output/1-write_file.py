#!/usr/bin/python3
"""The write_file function"""


def write_file(filename="", text=""):
    """function that writes a string to a text file (UTF8) and
    returns the number of characters written.
    """
    with open(filename, "w") as f:
        return f.write(text)
