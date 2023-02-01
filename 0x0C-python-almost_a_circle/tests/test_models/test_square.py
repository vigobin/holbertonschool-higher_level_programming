#!/usr/bin/python3
"""Unit testing classes"""
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """Defines the test class for Square"""

    def test_objects(self):
        a = Square(1)
        b = Square(4)
