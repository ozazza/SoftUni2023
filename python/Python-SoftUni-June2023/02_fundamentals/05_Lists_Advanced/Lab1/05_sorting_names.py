names = input().split(', ')
names.sort()
sorted_names = sorted(names, key=len, reverse=True)

print(sorted_names)
