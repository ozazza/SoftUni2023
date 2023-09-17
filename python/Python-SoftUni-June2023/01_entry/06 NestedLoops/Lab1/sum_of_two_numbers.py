# Input
range_start = int(input())
range_end = int(input())
magic_number = int(input())

# Logic
counter = 0
is_found = False
for i in range(range_start, range_end + 1):
    for m in range(range_start, range_end + 1):

        counter += 1
        if i + m == magic_number:

            is_found = True
            print(f'Combination N:{counter} ({i} + {m} = {magic_number})')
            break

    if is_found:
        break

# Output
if not is_found:
    print(f'{counter} combinations - neither equals {magic_number}')