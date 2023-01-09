#!/usr/bin/python3
"""class MyInt"""


class MyInt(int):
    """defines instance new*"""
    def __new__(cls, *args, **kwargs):
        """crete mode"""
        return super(MyInt, cls).__new__(cls, *args, **kwargs)

    def __eq__(self, inverted):
        """invert != to =="""
        return int(self) != inverted

    def __ne__(self, inverted):
        """invert == to !="""
        return int(self) == inverted
