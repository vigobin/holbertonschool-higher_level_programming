#!/usr/bin/python3
"""Defines the inherits from class function"""


def inherits_from(obj, a_class):
    """Functions that checksif the object is an instance of a class that
    inherited (directly or indirectly) from the specified class.
    """
    if not isinstance(obj, a_class) or type(obj) is not a_class:
        return True
    else:
        return False
