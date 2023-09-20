n = int(input())

for i in range(1, n + 1):

    sum_n = 0
    is_special = False
    for c in str(i):
        sum_n += int(c)

    if sum_n == 5 or sum_n == 7 or sum_n == 11:
        is_special = True

    print(f'{i} -> {is_special}')
