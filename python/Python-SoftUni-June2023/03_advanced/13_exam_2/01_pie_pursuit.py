from collections import deque

person_capacity = deque([int(x) for x in input().split()])
pies_stack = [int(x) for x in input().split()]

while person_capacity and pies_stack:
    curr_p_capacity = person_capacity[0]
    curr_pie = pies_stack[-1]

    if curr_p_capacity >= curr_pie:
        curr_p_capacity -= curr_pie
        pies_stack.pop()

        if curr_p_capacity > 0:
            person_capacity.append(curr_p_capacity)

    elif curr_p_capacity < curr_pie:
        curr_pie -= curr_p_capacity
        pies_stack.pop()

        if curr_pie > 1:
            pies_stack.append(curr_pie)
        elif curr_pie == 1:
            if len(pies_stack) > 1:
                next_pie = pies_stack.pop()
                next_pie += 1
                pies_stack.append(next_pie)
            else:
                pies_stack.append(curr_pie)

    person_capacity.popleft()

if len(pies_stack) <= 0 < len(person_capacity):
    print('We will have to wait for more pies to be baked!')
    print(f"Contestants left: {', '.join(str(capacity) for capacity in person_capacity)}")

elif len(pies_stack) <= 0 >= len(person_capacity):
    print('We have a champion!')

elif len(pies_stack) > 0 >= len(person_capacity):
    print('Our contestants need to rest!')
    print(f"Pies left: {', '.join(str(pie) for pie in pies_stack)}")
