#!/usr/bin/python3
"""The MYList class"""


class MyList(list):
    """class MyList that inherits from list.
    """
    def print_sorted(self):
        """prints the list in ascending order.
        """
        print(sorted(self))
