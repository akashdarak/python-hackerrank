#!/bin/python3

import math
import os
import random
import re
import sys

# repeatedString function
def repeatedString(s, n):
    repeat = ""
    for i in range(n):
        repeat = repeat + s
 
        if len(repeat) > n:
            break

    final = repeat[:n]
    return(final.count("a")) 


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    n = int(input())

    result = repeatedString(s, n)
    fptr.write(str(result) + '\n')

    fptr.close()
