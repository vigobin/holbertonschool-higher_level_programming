#!/usr/bin/python3
"""Unit testing classes"""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Defines the test class for Rectangle"""

    def test_objects(self):
        a = Rectangle(1, 1)
        b = Rectangle(1, 2, 0, 0, 1)
