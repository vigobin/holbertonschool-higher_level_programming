#!/usr/bin/python3
"""This is the square class"""


class Square:
    """This class defines a square by it's private instance attribute size
    """
    def __init__(self, size):
        """Instantation with size
        Args:
            size (_no type_): size of square
        """
        self.__size = size
