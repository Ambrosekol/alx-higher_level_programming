#!/usr/bin/python3
"""
This module contains code of a class named MyList
that inherits from list
"""


class MyList(list):
    """
    This is a class that has Public instance
    method: def print_sorted(self): that prints the list,
    but sorted (ascending sort)
    """
    def print_sorted(self):
        """This function prints a sorted list"""
        srtlist = sorted(self)
        print(srtlist)
