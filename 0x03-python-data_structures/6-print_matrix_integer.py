#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        indx = len(row) - 1
        while indx >= 0:
            print("{:d}".format(row[indx]), end="")
            if indx != 0:
                print(" ")
        print()
