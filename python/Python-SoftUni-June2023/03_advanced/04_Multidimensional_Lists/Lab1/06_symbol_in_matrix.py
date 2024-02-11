n = int(input())

matrix = []
for i in range(n):
    row = [x for x in input()]
    matrix.append(row)

symb = input()
is_found = False
for j in range(n):
    for m in range(len(matrix[j])):
        if symb == matrix[j][m]:
            print(f'({j}, {m})')
            is_found = True
            exit()

if not is_found:
    print(f'{symb} does not occur in the matrix')
