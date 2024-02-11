rows, cols = [int(x) for x in input().split(', ')]

matrix = []

max_sum = float('-inf') # most minimal number - minus infinity

i_left, i_right, i_down_left, i_down_right = 0, 0, 0, 0
for _ in range(rows):
    matrix.append([int(x) for x in input().split(', ')])

for row_i in range(rows - 1):
    for col_i in range(cols - 1):
        top_left = matrix[row_i][col_i]
        top_right = matrix[row_i][col_i + 1]
        down_left = matrix[row_i + 1][col_i]
        down_right = matrix[row_i + 1][col_i + 1]

        sum_els = top_right + top_left + down_left + down_right
        if sum_els > max_sum:
            max_sum = sum_els
            i_left, i_right, i_down_left, i_down_right = top_left, top_right, down_left, down_right

print(f'{i_left} {i_right}')
print(f'{i_down_left} {i_down_right}')
print(max_sum)
