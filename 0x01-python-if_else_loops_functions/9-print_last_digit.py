#!/usr/bin/python3
def print_last_digit(number):
    val = number
    if val < 0:
        val *= (-1)
        val = number % 10
    else:
        val = number % 10
    print("{}".format(val), end="")
    return val
