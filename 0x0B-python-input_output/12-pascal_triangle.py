#!/usr/bin/python3
"""Pascal's Triangle"""


def pascal_triangle(n):
    """Returns a list of lists of integers representing the
    Pascal's triangle of n"""
    if n <= 0:
        return []
