#!/usr/bin/python3
"""The Full rectangle class"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class Rectangle that inherits from BaseGeometry.
    """
    def __init__(self, width, height):
        """Instantiation with width and height
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        return (self.__width * self.__height)

    def __str__(self) -> str:
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
