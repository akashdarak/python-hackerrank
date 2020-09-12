
'''

Given a non-empty array of integers, return the k most frequent elements.

Input: nums = [1,1,1,2,2,3,4], k = 2
Output: [1,2]

'''
######################
#   List of Numbers
######################


num = [1,2,2,3,3,3,3,4] 
z = 2
di = {}

for x in num:
    k = x
    v = num.count(x)
    di[k] = v

print(di.items())

for a in sorted(di, key=di.get, reverse=True):
    print(a, di[a])
    

    
######################
#   List of String
######################
def dsort(l, k):
    d = {}
    newl = []

    for x in l:
        d[x] = l.count(x)

    
    for i in sorted(d, key=d.get, reverse=True):
        newl.append(i)
        print(i, d[i])
        
    newl = newl[:k]
    return newl

li = ["ant","ant","ant","ant", "cat", "ball", "ball"]
k = 2

final = dsort(li, k)
print(final)


