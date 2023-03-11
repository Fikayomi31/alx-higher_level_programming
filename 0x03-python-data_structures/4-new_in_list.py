#!/usr/bin/python3

def new_in_list(my_list, idx, new_element):
    new_list = my_list.copy()
    if idx < 0 or idx > len(my_list):
        return my_list
    else:
        new_list[idx] = new_element
        return new_list
    return my_list
