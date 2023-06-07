#!/usr/bin/python3
def fizzbuzz():
    for val in range(1, 101):
        if (val % 3) == 0 and (val % 5) == 0:
            print("FizzBuzz ", end="")
        elif (val % 3) == 0:
            print("Fizz ", end="")
        elif (val % 5) == 0:
            print("Buzz", end="")
        else:
            print("{} ".format(val), end="")
