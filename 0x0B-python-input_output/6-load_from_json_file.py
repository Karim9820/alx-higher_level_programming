#!/usr/bin/python3

"""
defines function
"""
import json


def load_from_json_file(filename):
    """open file"""
    with open(filename, "r", encoding="utf=8") as fl:
        """load obj from created json file"""
        return json.load(fl)
