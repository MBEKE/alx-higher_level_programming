#!/usr/bin/python3
import sys

argc = len(sys.argv) - 1
if argc == 0:
    print(0)
else:
    result = 0
    for i in range(1, argc + 1):
        result += int(sys.argv[i])
    print(result)
