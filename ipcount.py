import re

with open("log.txt") as file:
    lines = file.readlines()
    
pattern = '\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
ip = []

for l in lines:
    #ip.append(l.search(pattern))
    final = re.findall(pattern, l)
    print(final)
