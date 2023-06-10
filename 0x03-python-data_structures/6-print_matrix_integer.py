#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        indx = len(row) - 1
        a = 0
        while a <= indx:
            print("{:d}".format(row[a]), end="")
            if a != indx:
                print(" ", end="")
            a += 1
        print()
