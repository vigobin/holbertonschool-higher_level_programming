#!/usr/bin/python3
"""Adds arguments to a list"""


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

args = load_from_json_file("add_item.json")
save_to_json_file(args, "add_item.json")
