#!/usr/bin/python3
import sys

argv = sys.argv[1:]
argc = len(argv)

if argc == 0:
    print("0 arguments.")
elif argc == 1:
    print("1 argument:")
    print(f"1: {argv[0]}")
else:
    print(f"{argc} arguments:")
    for i, arg in enumerate(argv, start=1):
        print(f"{i}: {arg}")
