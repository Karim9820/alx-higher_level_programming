#!/usr/bin/python3
"""Defines a peak-finding algorithm."""


def find_peak(list_of_integers):
    """ Finds the peak in a list of integers """
    if list_of_integers == []:
        return None

    length = len(list_of_integers)
    m = int(length / 2)
    loi = list_of_integers

    if m - 1 < 0 and m + 1 >= length:
        return loi[m]
    elif m - 1 < 0:
        return loi[m] if loi[m] > loi[m + 1] else loi[m + 1]
    elif m + 1 >= length:
        return loi[m] if loi[m] > loi[m - 1] else loi[m - 1]

    if loi[m - 1] < loi[m] > loi[m + 1]:
        return loi[m]

    if loi[m + 1] > loi[m - 1]:
        return find_peak(loi[m:])
    return find_peak(loi[:m])
