def addTwoDigits(n):
    sum = 0
    while(n != 0):
        sum = sum + int(n%10)
        n = int(n/10)
    return sum
    
n = 92
print(addTwoDigits(n)) 
