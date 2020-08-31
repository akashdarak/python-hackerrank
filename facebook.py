
def get_num_stickers(inp):
  strin = "facebok"
  c = 0
  cnew = 1
  for i in range(len(strin)):
    if inp.count(strin[i]) > 0 and cnew > c:
      cnew = inp.count(strin[i])
  return cnew

if __name__ == '__main__':
    inp = input("Please input the string: ")
    stickers = get_num_stickers(inp)
    print(stickers)
