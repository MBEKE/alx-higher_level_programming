def replace_in_list(my_list, idx, element):
    """Replace an element of a list at a specific position"""
    if idx < 0 or idx >= len(my_list):
        return my_list.copy   # return a copy of the original list

    new_list = my_list.copy()  # create a copy of the original list
    new_list[idx] = element  # replace the element at given index
    return new_list
