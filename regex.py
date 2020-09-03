
import re

def test():
    for i in range(len(s)):
        s = s[i, i + int(len(k))]
        m = re.search(k, s)
        print(m.start())
        print(m.end())
    

def working():
    temp = 0
    for i in range(len(s)):
        if (s[i:i+len(k)]) == k:
            print('({}, {})'.format(i,i+len(k)-1))
            temp = 1
    
    if temp == 0:
        print("(-1, -1)")


s = input()
k = input()

test()
working()
