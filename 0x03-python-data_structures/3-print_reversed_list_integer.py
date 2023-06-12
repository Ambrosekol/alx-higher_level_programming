#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    length = len(my_list)
    newlst = [my_list[val] for val
              in range((length - 1), -1, -1)]
    for num in newlst:
        print("{:d}".format(num))
