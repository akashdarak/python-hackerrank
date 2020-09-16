
def anagram(strs):
    d = {}
    for i in strs:
        x = ''.join(sorted(i))
        if x in d:
            d[x].append(i)
        else:
            d[x] = [i]
    print(d.values())
    

string = ["eat", "tea", "tan", "ate", "nat", "bat"]
anagram(string)
