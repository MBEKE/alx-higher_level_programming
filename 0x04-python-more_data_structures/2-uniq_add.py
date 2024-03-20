#!/usr/bin/python3
def uniq_add(my_list=[]):
    """ addd all unique intergers in a list(only once for each interger)"""
    sum = 0
    unique = set(my_list)
    for integer in unique:
            sum += integer
    return sum
