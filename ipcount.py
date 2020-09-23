import re

with open("log.txt") as file:
    lines = file.readlines()
    
pattern = '\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
ip = []
d ={}

for l in lines:
    final = re.findall(pattern, l)
    final = (','.join(final))
    #print(final)
    ip.append(final)
    if final in d:
        d[final] += 1 
    else:
        d[final] = 1
        
print(ip)
print(d)   
