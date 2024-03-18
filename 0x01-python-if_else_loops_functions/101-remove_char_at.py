#!/usr/bin/python3
def remove_char_at(str, n):
    newString = ""
    for i in range(len(str)):
        if i == n:
            continue
        else:
            newString += str[i]
    return newString
