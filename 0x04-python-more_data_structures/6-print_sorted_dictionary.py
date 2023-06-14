#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    dicList = sorted(list(a_dictionary))
    for var in dicList:
        print("{}".format(a_dictionary[var]))
