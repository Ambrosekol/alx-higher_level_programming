#!/usr/bin/python3
def print_last_digit(number):
    val = number
    if val < 0:
        val = val * (-1)
        val = val % 10
    else:
        val = val % 10
    print("{}".format(val), end="")
    return val
