# Imagine you are given a plain text, ASCII, English document, something like a
# book from Project Gutenberg. Develop a concordance for the book -- the number
# of times each word appears -- and then print the top N most frequent words and
# how many times they occur. N can be either hardcoded or a parameter.

# Example call and output:
# $ ./concordance book.txt 10
# the     8230
# and     5067
# of      4139
# to      3651
# a       3017
# in      2659
# it      2082
# his     2008
# i       1972
# that    1950



with open("log.txt") as f:
    lines = f.readlines()
    d = {}
    
    for l in lines:
        print(l)
        s = l.split(" ")
        #print(s)
        for i in s:
            if i not in d:
                d[i] = 1 
            else:
                d[i] += 1
    print(d)   
