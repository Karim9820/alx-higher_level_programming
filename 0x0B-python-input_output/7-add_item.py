#!/usr/bin/python3

"""
script that adds all arguments to a Python list, and then save them to a file
"""

import json
from sys import argv

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

"""
Define file for saving
"""
filename = "add_item.json"

try:
    json_list = load_from_json_file(filename)
except FileNotFoundError:
    """create new if file not found"""
    json_list = []

"""
add all arguments
"""
for arg in argv[1:]:
    """append module"""
    json_list.append(arg)
    """saving to file"""

save_to_json_file(json_list, filename)
