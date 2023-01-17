#!/usr/bin/python3
"""This is the square class"""


class Square:
    """Defines a square
    """
    def __init__(self, size=0):
        """Initialize a square

        Args:
            size (int): size of the sqaure.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
