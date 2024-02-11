rows, cols = [int(x) for x in input().split(', ')]

matrix = []
for i in range(rows):
    data = [int(x) for x in input().split(' ')]
    matrix.append(data)

for col in range(cols):
    sum_col = 0
    for row in range(rows):
        sum_col += matrix[row][col]

    print((sum_col))
