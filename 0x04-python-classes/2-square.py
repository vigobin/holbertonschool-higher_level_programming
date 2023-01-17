#!/usr/bin/python3
"""Create a class Square"""


class Square:
    """Defining a square
    """
    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size (int): The size of a new square.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """returns square area
        """
        return (self.__size * self.__size)
