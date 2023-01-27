#!/usr/bin/python3
"""The class square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class Square that inherits from Rectangle.
    """
    def __init__(self, size):
        """Instantiation with size
        """
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        "Area method"
        return (self.__size * self.__size)

    def __str__(self) -> str:
        return ("[Square] {}/{}".format(self.__size, self.__size))
