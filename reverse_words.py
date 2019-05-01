import sys
import os

s ="i like this program"		#Reverse words in a string
words =s.split() 	
string =[] 

for word in words: 
    string.insert(0, word) 
  
print("Reversed String:") 
print(" ".join(string)) 

