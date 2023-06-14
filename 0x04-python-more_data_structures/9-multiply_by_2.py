#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    newDic = {}
    for k, v in a_dictionary.items():
        newDic[k] = v * 2
    return newDic
    