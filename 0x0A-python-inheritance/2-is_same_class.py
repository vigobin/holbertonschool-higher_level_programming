#!/usr/bin/python3
"""Is same class function"""


def is_same_class(obj, a_class):
    """Function that checks if an object is exactly and instance of the class.
    """
    if type(obj) is a_class:
        return True
    else:
        return False
