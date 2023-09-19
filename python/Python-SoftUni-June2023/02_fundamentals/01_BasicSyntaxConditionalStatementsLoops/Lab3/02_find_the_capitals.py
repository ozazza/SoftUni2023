txt = input()

capitals = []
for i in range(len(txt)):

    if txt[i].isupper():
        capitals.append(i)

print(capitals)
