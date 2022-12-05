#!/usr/bin/python3

def max_integer(my_list=[]):
    if len(my_list) == 0:
        return

    maxint = my_list[0]
    for i in range(1, len(my_list)):
        if maxint < my_list[i]:
            maxint = my_list[i]
        else:
            continue
    return (maxint)
