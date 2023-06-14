#!/usr/bin/python3

def best_score(a_dictionary):
    vl = 0
    ky = ""
    if a_dictionary == None:
        return None
    for key, val in a_dictionary.items():
        if val > vl:
            ky = key
            vl = val
    return ky
