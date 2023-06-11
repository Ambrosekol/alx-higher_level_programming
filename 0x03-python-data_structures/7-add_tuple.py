#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    lst = list(tuple_a)
    lst1 = list(tuple_b)
    newlst = list()
    default = 0
    while len(lst) < 2:
        lst.append(default)
    while len(lst1) < 2:
        lst1.append(default)
    while len(newlst) < 2:
        newlst.append(lst[default] + lst1[default])
        default += 1
    return tuple(newlst)
