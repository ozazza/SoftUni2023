def get_next_position(position, direction_mapper, direction):
    row_i, col_i = position
    row_move, col_move = direction_mapper[direction]

    row_index_next_move = row_i + row_move
    col_index_next_move = col_i + col_move

    return row_index_next_move, col_index_next_move


n = int(input())

matrix = []
position = None

jet = 'J'
enemy = 'E'
repair = 'R'
empty = '-'

armor_jet = 300
enemies = 4

direction_mapper = {
    'up': (-1, 0),
    'down': (1, 0),
    'right': (0, 1),
    'left': (0, -1),
}

col_i = 0
for row_i in range(n):
    data = list(input())

    if jet in data:
        col_i = data.index(jet)
        position = [row_i, col_i]

    matrix.append(data)

command = input()

while armor_jet > 0 and enemies > 0:
    next_row_i, next_col_i = get_next_position(position, direction_mapper, command)
    curr_row_i, curr_col_i = position

    sign = matrix[next_row_i][next_col_i]
    matrix[curr_row_i][curr_col_i] = empty
    matrix[next_row_i][next_col_i] = jet
    position = [next_row_i, next_col_i]

    if sign != empty:

        if sign == enemy:
            enemies -= 1
            if enemies > 0:
                armor_jet -= 100

        elif sign == repair:
            armor_jet = 300

    command = input()

if enemies == 0:
    print('Mission accomplished, you neutralized the aerial threat!')
if armor_jet < 1:
    print(f'Mission failed, your jetfighter was shot down! Last coordinates [{position[0]}, {position[1]}!')

for row in matrix:
    print(f'{"".join(row)}')
