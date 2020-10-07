'''
Write code to produce the following output:

1 0 1 0 1
0 1 0 1 0
1 0 1 0 1
0 1 0 1 0
1 0 1 0 1
'''

def printMatrix():
    n = 5
    s = ""
    b = str(0)
    
    for i in range(n):
        for j in range(n):
            d = getnext(b)
            b = d
            s = s + d
        print(s)
        s = ""
        
def getnext(b):
    if b == str(0):
        return(str(1))
    else:
        return(str(0))

printMatrix()
