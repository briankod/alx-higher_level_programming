#!/usr/bin/python3
"""
A class MyList that inherits from list
"""


class MyList(list):
    """Derived class of super class list"""
    def print_sorted(self):
        """prints the sorted list (ascending sort)"""
        print(sorted(self))
