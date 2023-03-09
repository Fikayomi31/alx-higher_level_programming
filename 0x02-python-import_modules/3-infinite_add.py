#!/usr/bin/python3
import sys
result = 0
for arg in sys.argv[1:]:
    result += int(arg)
print(result)
