#!/usr/bin/python3
for letter in range(122, 96, -1):
    if letter % 2 == 0:
        n = chr(letter)
    else:
        n = chr(letter - 32)
    print("{}".format(letter), end="")
