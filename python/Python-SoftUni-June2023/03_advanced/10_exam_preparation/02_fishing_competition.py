def get_next_position(position, direction_mapper, direction, matrix):
    row_i, col_i = position
    row_move, col_move = direction_mapper[direction]

    row_index_next_move = row_i + row_move
    col_index_next_move = col_i + col_move

    if 0 <= row_index_next_move < len(matrix) and 0 <= col_index_next_move < len(matrix):
        return row_index_next_move, col_index_next_move

    if 0 > row_index_next_move:
        row_index_next_move = len(matrix) - 1
    elif row_index_next_move >= len(matrix):
        row_index_next_move = 0
    if 0 > col_index_next_move:
        col_index_next_move = len(matrix[0]) - 1
    elif col_index_next_move >= len(matrix):
        col_index_next_move = 0

    return row_index_next_move, col_index_next_move


n = int(input())

direction_mapper = {
    'up': (-1, 0),
    'down': (1, 0),
    'right': (0, 1),
    'left': (0, -1),
}

matrix = []
position = None
count_fishes = 0

for row_index in range(n):
    data = list(input())

    if 'S' in data:
        curr_col = data.index('S')
        position = [row_index, curr_col]

    matrix.append(data)

command = input()

while command != 'collect the nets':
    curr_row_index, curr_col_index = position
    next_row_index, next_col_index = get_next_position(position, direction_mapper, command, matrix)

    symbol = matrix[next_row_index][next_col_index]
    matrix[next_row_index][next_col_index] = 'S'
    matrix[curr_row_index][curr_col_index] = '-'
    position = [next_row_index, next_col_index]

    if symbol.isdigit():
        count_fishes += int(symbol)
    elif symbol == 'W':
        print(f'You fell into a whirlpool! '
              f'The ship sank and you lost the fish you caught. '
              f'Last coordinates of the ship: [{",".join([str(x) for x in position])}]')
        exit()

    command = input()

if count_fishes >= 20:
    print(f'Success! You managed to reach the quota!')
else:
    print(f"You didn't catch enough fish and didn't reach the quota! "
          f"You need {20 - count_fishes} tons of fish more.")

if count_fishes > 0:
    print(f'Amount of fish caught: {count_fishes} tons.')

for row in matrix:
    print(f'{"".join(row)}')

