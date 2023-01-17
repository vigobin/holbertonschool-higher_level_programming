#!/usr/bin/python3
"""Create a Square class"""


class Square:
    """Defines a square
    """
    def __init__(self, size=0):
        """Initialize a new square

        Args:
        size (int): size of new square.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """Retrieve size of square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of square
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the area of square
        """
        return (self.__size * self.__size)
