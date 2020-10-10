openl = ["[", "{", "("]
closel = ["]", "}", ")"]

stack = []
expression = "{}[()]"

for i in expression:
    if i in openl:
        stack.append(i)
    elif i in closel:
        pos = closel.index(i)
        print("Position:", pos)
        if (openl[pos] == stack[len(stack)-1]):
            stack.pop()
        else:
            print("Unbalanced")
            break

if len(stack) == 0:
    print("Balanced")
