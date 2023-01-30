#!/usr/bin/python3
""" A script that add all arguments to a Python list and save them to a file
"""
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

args_lists = load_from_json_file("add_item.json")

for args in sys.argv[1:]:
    args_lists.append(args)

save_to_json_file(args_lists, "add_item.json")
