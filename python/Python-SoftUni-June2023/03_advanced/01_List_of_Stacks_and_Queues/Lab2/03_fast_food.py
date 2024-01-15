from collections import deque

qty_day = int(input())
qty_order = deque([int(x) for x in input().split()])

print(max(qty_order))

for _ in range(len(qty_order)):
    if qty_day - qty_order[0] >= 0:
        qty_day -= qty_order.popleft()
    else:
        break

if len(qty_order) > 0:
    print('Orders left:', end=' ')
    print(*qty_order, sep=' ')
else:
    print('Orders complete')
