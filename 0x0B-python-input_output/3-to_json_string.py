#!/usr/bin/python3
import json
"""
This module contains all a a function that returns the
JSON representation of an object (string)
"""


def to_json_string(my_str):
    """
    this accepts an object and then the function
    returns the JSON representation of an object (string)
    """
    return json.dump(my_str)
