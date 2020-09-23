#We suspect we are under an SSH brute-force attack from a small number of remote IP addresses. 
#We would like to analyze the appropriate log file to get a count of failed login attempts from each remote IP address. 
#How would you do this with a simple script in Python/Bash/(your preferred language) given the following sample log entry:

#log.txt
#Jan 30 11:08:25 prod-db-01 sshd[30067]: Failed password for hacker from 192.168.1.2 port 43367 ssh2
#Jan 30 11:08:25 prod-db-01 sshd[30067]: Failed password for hacker from 192.168.1.3 port 43367 ssh2
#Jan 30 11:08:25 prod-db-01 sshd[30067]: Failed password for hacker from 192.168.1.2 port 43367 ssh2
#Jan 30 11:08:25 prod-db-01 sshd[30067]: Failed password for hacker from 192.168.1.4 port 43367 ssh2

#Output
#192.168.1.2 2
#192.168.1.3 1
#192.168.1.4 1

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
