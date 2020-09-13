#!/bin/python

import math
import os
import random
import re
import sys

# Rotate Left function
def rotLeft(a, d):
    return a[d:] + a[:d]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = raw_input().split()
    n = int(nd[0])
    d = int(nd[1])

    a = map(int, raw_input().rstrip().split())
    result = rotLeft(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

###############################################################
    
def rotate(arr, z):
    newarr = []
    for i in range(z, len(arr)):
        newarr.append(arr[i])

    for j in range(z):
        newarr.append(arr[j])
        
    return newarr


arr = [10, 20, 30, 40, 50]
z=3

print(rotate(arr,z))
