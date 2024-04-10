rows = int(input())

matrix = []
for i in range(rows):
    data = [int(x) for x in input().split(', ') if int(x) % 2 == 0]
    matrix.append(data)

print(matrix)
