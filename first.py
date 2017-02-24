#!/usr/bin/env python3

def evenMem(aList):
    result = []
    for item in aList:
        if item % 2 == 0:
            result.append(item)
    return result

print(evenMem([1,2,3,4]))
