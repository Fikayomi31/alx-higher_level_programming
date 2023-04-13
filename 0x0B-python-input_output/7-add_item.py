#!/usr/bin/python3

import sys
import json

def save_to_json_file(my_obj, filename):
    with open(filename, 'w') as f:
        json.dump(my_obj, f)

def load_from_json_file(filename):
    with open(filename, 'r') as f:
        return json.load(f)

# Load existing list from file, if available
try:
    my_list = load_from_json_file('add_item.json')
except FileNotFoundError:
    my_list = []

# Add command line arguments to the list
for arg in sys.argv[1:]:
    my_list.append(arg)
save_to_json_file(my_list, 'add_item.json')
