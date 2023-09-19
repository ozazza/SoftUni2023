n = input()

list_n = []

for i in n:
    list_n.append(i)

list_n.sort(reverse=True)
largest = ''.join(list_n)

print(largest)
