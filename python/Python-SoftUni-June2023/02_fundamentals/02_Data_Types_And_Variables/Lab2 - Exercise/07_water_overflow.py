lines = int(input())
capacity = 255

added = 0
for i in range(lines):

    added_qty = int(input())

    if added_qty <= capacity:
        added += added_qty
        capacity -= added_qty
    else:

        print('Insufficient capacity!')
        continue

if capacity >= 0:
    print(added)
else:
    print(0)
