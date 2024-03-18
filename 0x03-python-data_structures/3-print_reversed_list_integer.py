def print_reversed_list_integer(my_list=[]):
    """Print all intergers of a list in reverse order."""
    if not my_list:
        return

    for i in reversed(my_list):
        print("{:d}".format(i))
