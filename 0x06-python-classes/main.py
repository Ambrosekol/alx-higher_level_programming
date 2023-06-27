#!/usr/bin/python3
Square = __import__('2-square').Square

try:
    my_square_3 = Square(2)
    print(type(my_square_3))
    print(my_square_3.__dict__)
except Exception as e:
    print(e)