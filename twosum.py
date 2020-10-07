def twosum(arr, z):
    final = []
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == z:
                final.append([arr[i], arr[j]])
    return final
 
arr = [2,7,3,11,5,4,6]
z=9 

print(twosum(arr,z))


#########################################################
#   O(1) Complexity using Dictionary


l = [1, 2, 5, 6, 8, 4, 9, 12, 3]
total = 7

d = {}

for i in range(len(l)):
    diff = total - l[i]
    if diff in d:
        print(diff, l[i])
    d[l[i]] = l[i]
