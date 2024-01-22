n = int(input())

odd = set()
even = set()

result = set()
for i in range(n):
    name = input()
    score = 0

    for char in name:
        score += ord(char)
    score //= (i + 1)

    if score % 2 == 0:
        even.add(score)
    else:
        odd.add(score)

if sum(odd) == sum(even):
    result = odd.union(even)
elif sum(odd) > sum(even):
    result = odd.difference(even)
elif sum(odd) < sum(even):
    result = odd.symmetric_difference(even)

print(*result, sep=', ')
