#!/usr/bin/python3
"""The square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Defines the class Square which inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize the square"""
        super().__init__(width=size, height=size, x=x, y=y, id=id)
