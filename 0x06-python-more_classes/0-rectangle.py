#!/usr/bin/python3
"""Rectangle class."""


class Rectangle:
    """Defines a rectangle"""
    def __init__(self, width=0, height=0):
        """Instantation of a rectangle.

        Args:
            width (int): Rectangle width. Defaults to 0.
            height (int): Rectangle Height. Defaults to 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
