#!/usr/bin/python3
"""script that adds all arguments to a Python list, then saves to a file
"""


from sys import argv


save = __import__('7-save_to_json_file').save_to_json_file
load = __import__('8-load_from_json_file').load_from_json_file


try:
    s = load("add_item.json")
except FileNotFoundError:
    s = []
for i in argv[1:]:
    s.append(i) 

save(s, "add_item.json")
