n = int(input())

collect = set()
for i in range(n):
    collect.add(input())

print(*collect, sep='\n')
