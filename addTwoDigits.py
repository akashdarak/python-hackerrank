def addTwoDigits(n):
    sum = 0
    while(n != 0):
        sum = sum + int(n%10)
        n = int(n/10)
    return sum

def digitsManipulations(n):
    m = n
    
    prod = 1
    while(n != 0):
        prod = prod*(int(n%10))
        n = int(n/10)
    
    total = 0
    while(m != 0):
        total = total + int(m%10)
        m = int(m/10)
    
    final = prod - total
    return final
    
n = 92
print(addTwoDigits(n)) 

print(digitsManipulations(n))
