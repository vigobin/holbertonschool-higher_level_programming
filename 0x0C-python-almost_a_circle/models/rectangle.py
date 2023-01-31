#!/usr/bin/python3
"""The Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Defines the Rectangle class which inhereits from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returns the area value of the Rectangle instance"""
        return self.__width * self.__height

    def display(self):
        """prints in stdout the Rectangle instance with the character #
            y is newline, x is space"""
        print("\n" * self.__y, end="")
        for row in range(self.__height):
            print((" " * self.__x) + ("#" * self.__width))

    def __str__(self):
        """Override str to return formatted info"""
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x,
                                                        self.__y, self.__width,
                                                        self.__height))

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        if len(args) > 0:
            attributes = ["id", "width", "height", "x", "y"]
            for arguments in range(len(args)):
                setattr(self, attributes[arguments], args[arguments])

        if kwargs is not None:
            for k, v in kwargs.items():
                setattr(self, k, v)
