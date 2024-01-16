from collections import deque

sequence = deque(x for x in input())
half_sq_len = int(len(sequence) / 2)
list_is_closed = []

compared_sq = sequence.copy()
compared_one_by_one = sequence.copy()
closed_symbol = ''

if len(sequence) > 0 and len(sequence) % 2 == 0:
    while compared_sq:
        open_symbol = compared_sq.popleft()
        last = compared_sq.pop()

        if open_symbol == '(':
            closed_symbol = ')'
        elif open_symbol == '{':
            closed_symbol = '}'
        elif open_symbol == '[':
            closed_symbol = ']'

        if last == closed_symbol:
            list_is_closed.append(True)
        else:
            break

    if len(list_is_closed) != half_sq_len:

        list_is_closed = []
        for i in range(0, len(compared_one_by_one) - 1, 2):
            j = i + 1

            if compared_one_by_one[i] == '(':
                closed_symbol = ')'
            elif compared_one_by_one[i] == '{':
                closed_symbol = '}'
            elif compared_one_by_one[i] == '[':
                closed_symbol = ']'

            if closed_symbol == compared_one_by_one[j]:
                list_is_closed.append(True)
            else:
                break

if len(sequence) > 0 and len(list_is_closed) == half_sq_len:
    print('YES')
else:
    print('NO')
