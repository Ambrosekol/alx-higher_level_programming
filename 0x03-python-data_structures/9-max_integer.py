#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return 0
    else:
        point = 0
        end = len(my_list)
        while point < end:
            point2 = end - 1
            while point2 > point:
                if my_list[point2] < my_list[point]:
                    temp = my_list[point2]
                    my_list[point2] = my_list[point]
                    my_list[point] = temp
                point2 -= 1
            point += 1
        return my_list[end - 1]
