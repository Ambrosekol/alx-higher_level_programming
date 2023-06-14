#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newlist = list()
    for row in matrix:
        newlist.append(list(map(
            lambda x: x **2, row)))
    return newlist
