#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    new_dict = dict(a_dictionary)  # Create a copy of the original dictionary
    keys_to_delete = [k for k, v in new_dict.items() if v == value]
    for key in keys_to_delete:
        del new_dict[key]
    return new_dict
