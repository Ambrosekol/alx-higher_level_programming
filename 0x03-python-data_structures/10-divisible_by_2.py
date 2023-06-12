#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    new_arr = list()
    for val in my_list:
        if (val % 2) == 0:
            new_arr.append(True)
        else:
            new_arr.append(False)
    return new_arr
