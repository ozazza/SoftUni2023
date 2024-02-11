rows = int(input())

matrix = []
for i in range(rows):
    data = [int(x) for x in input().split(', ')]
    matrix.extend(data)

print(matrix)
