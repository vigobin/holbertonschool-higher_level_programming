#!/usr/bin/python3
"""Unit testing classes"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Defines the test class for Base"""
    def test_objects(self):
        Base._Base__nb_objects = 0
        self.assertEqual(Base._Base__nb_objects, 0)
