#!/usr/bin/python3
def delet_at(my_list=[], idx=0):
    """Delete the item at a specific position in a list"""
    if idx < 0 or index >= len(my_list):
        return my_list.copy()

    new_list = []
    for i, item in enumerate(my_list):
        if i != idx:
            new_list.append(item)

    return new_list
