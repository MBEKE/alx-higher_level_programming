#!/usr/bin/python3
def new_in_list(miy_list, idx, element):
    """Replace an element in a list at a specific position without modifying
    the orignal list"""
    if idx < 0 or idx >= len(miy_list):
        return miy_list.copy()

    new_list = miy_list.copy()
    new_list[idx] = element
    return new_list
