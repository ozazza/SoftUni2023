rows, cols = [int(x) for x in input().split(', ')]

total = 0
matrix = []
for i in range(rows):
    row_data = [int(x) for x in input().split(', ')]
    matrix.append(row_data)
    total += sum(row_data)

print(total)
print(matrix)
