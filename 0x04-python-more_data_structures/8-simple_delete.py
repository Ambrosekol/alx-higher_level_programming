#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    for elem in list(a_dictionary):
        if key == elem:
            del a_dictionary[key]
    return a_dictionary
