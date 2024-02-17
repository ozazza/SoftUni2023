from collections import deque

worms = [int(x) for x in input().split()]
holes = deque([int(x) for x in input().split()])

worms_counted = len(worms)
count_match = 0
while worms and holes:
    curr_worm = worms[-1]
    curr_hole = holes[0]

    if curr_worm == curr_hole:
        worms.pop()
        holes.popleft()
        count_match += 1

    else:
        holes.popleft()
        worms[-1] -= 3

        if worms[-1] <= 0:
            worms.pop()

if count_match > 0:
    print(f'Matches: {count_match}')
else:
    print('There are no matches.')

if not worms:
    if count_match == worms_counted:
        print('Every worm found a suitable hole!')
    elif count_match < worms_counted:
        print('Worms left: none')
elif worms:
    print(f'Worms left: {", ".join([str(x) for x in worms])}')

if not holes:
    print('Holes left: none')
else:
    print(f'Holes left: {", ".join([str(x) for x in holes])}')
