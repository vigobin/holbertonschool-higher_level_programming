#!/usr/bin/python3
"""Defines the function that prints a name"""


def say_my_name(first_name, last_name=""):
    """Print a name

    Args:
        first_name (str): Frist name to print.
        last_name (str): Last name.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
