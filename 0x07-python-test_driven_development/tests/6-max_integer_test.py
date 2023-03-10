#!/usr/bin/python3
"""Unittest for max_integer([..])"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Define unittests for max_integer([..]).
    """

    def test_max_int(self):
        """tests normal usage"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        """test if empty"""
        self.assertEqual(max_integer([]), None)
        """tests for negatives"""
        self.assertEqual(max_integer([-1, -3, -2, -4]), -1)
        """tests for one item"""
        self.assertEqual(max_integer([1]), 1)


if __name__ == '__main__':
    unittest.main()
