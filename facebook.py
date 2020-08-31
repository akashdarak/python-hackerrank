
def get_num_stickers(inp):
  strin = "facebok"
  c = 0
  cnew = inp.count(strin[0])
  for i in range(len(strin)):
    if (cnew > c):
      cnew = inp.count(strin[i])
      print(cnew)
  return cnew

if __name__ == '__main__':
    inp = input("Please input the string: ")
    stickers = get_num_stickers(inp)
    print(stickers)
