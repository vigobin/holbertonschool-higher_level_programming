#!/usr/bin/python3
"""The square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Defines the class Square which inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize the square"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value
