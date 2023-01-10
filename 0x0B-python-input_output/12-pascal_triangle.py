#!/usr/bin/python3
"""Defines a triangle"""


def pascal_triangle(n):
    """Reps Pascal's triangle"""
    if n <= 0:
        return []

    tr = [[1]]
    while len(tr) != n:
        tri = tr[-1]
        tmp = [1]
        """append to create list"""
        for i in range(len(tri) - 1):
            tmp.append(tri[i] + tri[i + 1])
        tmp.append(1)
        tr.append(tmp)
    return tr
