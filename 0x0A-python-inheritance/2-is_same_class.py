#!/usr/bin/python3

"""
This module contains a code for a function
that returns True if the object is exactly an instance
of the specified class ; otherwise False.
"""


def is_same_class(obj, a_class):
    """Returns true or false if it is an instance"""
    return type(obj) == a_class
