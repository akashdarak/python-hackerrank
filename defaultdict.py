
# Read input from STDIN. Print output to STDOUT
import sys
import os
from collections import defaultdict

lin = []
lim = []

n, m = input().split()

#for line in sys.stdin:
#    print(line)

count = 0
for line in sys.stdin:
    count += 1
    line = line.strip()
    lin.append(line)
    if int(count) == int(n):
        break
print(lin)

for line in sys.stdin:
    line = line.strip()
    lim.append(line)
print(lim)

#d = defaultdict(lambda: "-1")
