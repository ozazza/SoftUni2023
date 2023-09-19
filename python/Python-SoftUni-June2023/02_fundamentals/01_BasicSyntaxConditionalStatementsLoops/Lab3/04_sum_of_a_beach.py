word = input()

fillers = ['sand', 'water', 'fish', 'sun']
count = 0

for i in fillers:
    count += word.lower().count(i)

print(count)
