a = [1, 2, 3, 4, 5, 5]

for i in range(len(a)):
    left = 0
    right = 0
    for j in range(0, i):
        left += a[j]
    for j in range(i, len(a)):
        right += a[j]
        
    if left == right:
        print(a[:i])
        print(a[i:])
        break
