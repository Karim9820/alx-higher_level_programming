#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list and len(my_list):
        scr = 0
        cnt = 0
        for tup in my_list:
            scr += (tup[0] * tup[1])
            cnt += tup[1]
        return (scr / cnt)
    return 0
