#!/usr/bin/python3
import json
"""
This module contains all a function that returns an object
(Python data structure) represented by a JSON string
"""


def from_json_string(my_str):
    """
    this accepts an object and then returns an object
    (Python data structure) represented by a JSON string
    """
    return json.dump(my_str)
