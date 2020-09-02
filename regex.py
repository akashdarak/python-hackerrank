
import re

s = input()
k = input()

for i in range(len(s)):
    s = s[i, i + int(len(k))]
    m = re.search(k, s)
    print(m.start())
    print(m.end())
