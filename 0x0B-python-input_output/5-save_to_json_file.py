#!/usr/bin/python3

"""
defines function 
"""
import json


def save_to_json_file(my_obj, filename):
    """write file"""
    with open(filename, "w", encoding="utf=8") as fl:
        """write obj file"""
        json.dump(my_obj, fl)
