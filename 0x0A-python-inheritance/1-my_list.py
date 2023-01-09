#!/usr/bin/python3
"""
inherits from MyList
"""


class MyList(list):
    """sub + initialise """
    def __init__(self):
        super().__init__()

        """instance to print sorted list"""

    def print_sorted(self):
        print(sorted(self))
