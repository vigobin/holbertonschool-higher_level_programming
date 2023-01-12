#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = list(my_list)
    if idx < 0:
        return new_list
    elif idx >= len(new_list):
        return new_list
    else:
        new_list[idx] = element
        return new_list
