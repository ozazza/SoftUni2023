n = int(input())

opened = '('
closed = ')'
is_opened = False
result = 'BALANCED'
count_unbalance = 0
for i in range(n):
    ch = input()

    if ch is opened and is_opened is True:
        result = 'UNBALANCED'
        count_unbalance += 1
        continue

    if ch is opened:
        is_opened = True
        continue

    if ch is closed and is_opened is False:
        result = 'UNBALANCED'
        count_unbalance += 1
        continue

    if ch is closed and is_opened is True:
        is_opened = False
        continue

if not is_opened and count_unbalance == 0:
    print(result)
else:
    print('UNBALANCED')
