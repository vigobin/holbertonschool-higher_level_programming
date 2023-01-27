#!/usr/bin/python3
"""Defines the kind of class"""


def is_kind_of_class(obj, a_class):
    """Checks if the object is an instance of the class or if it's
    inherited from it"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
