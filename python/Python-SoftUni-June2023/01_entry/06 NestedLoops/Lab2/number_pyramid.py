# Input
n = int(input())

# Logic
counter = 0
is_end = False

for row in range(1, n + 1):
    for col in range(1, row + 1):
        counter += 1

        if counter > n:
            is_end = True
            break

        print(counter, end=' ')

    if is_end:
        break
    print()
