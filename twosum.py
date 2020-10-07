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
