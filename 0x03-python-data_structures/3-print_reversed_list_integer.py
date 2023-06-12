#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    newlst = [my_list[val] for val
              in range((len(my_list) - 1), -1)]
    for num in newlst:
        print("{:d}".format(num))
