#!/usr/bin/python3
"""Rectangle class"""


class Rectangle:
    """Defines a rectangle
    """
    def __init__(self, width=0, height=0):
        """Instantiate a rectangle.

        Args:
            width (int): Width of rectangle. Defaults to 0.
            height (int): Height of rectangle. Defaults to 0.
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

    def area(self):
        return (self.__width * self.__height)

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return ((self.__width + self.__height) * 2)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ("")
        print_rectangle = ""
        for i in range(self.__height):
            if i == self.__height - 1:
                print_rectangle += "#" * self.__width
            else:
                print_rectangle += "#" * self.__width + "\n"

        return print_rectangle
