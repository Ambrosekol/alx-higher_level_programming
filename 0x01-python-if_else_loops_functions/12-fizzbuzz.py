#!/usr/bin/python3
def fizzbuzz():
    for val in range(1, 101):
        if (val % 3) == 0 and (val % 5) == 0:
            print("FizzBuzz ")
        elif (val % 3) == 0:
            print("Fizz ")
        elif (val % 5) == 0:
            print("Buzz")
        else:
            print("{} ".format(val))
