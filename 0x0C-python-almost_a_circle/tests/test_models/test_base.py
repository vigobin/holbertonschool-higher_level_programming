#!/usr/bin/python3
"""Unit testing classes"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Defines the test class for Base"""

    def test_objects(self):
        a = Base(0)
        self.assertEqual(a.id, 0)
        b = Base(1)
        self.assertEqual(b.id, 1)


if __name__ == "__main__":
    unittest.main()
