num = int(input())

for i in range(1, num + 1):
    for m in range(0, i):
        print('*', end=' ')

    print()

for k in range(num - 1, 0, -1):
    for t in range(k, 0, -1):
        print('*', end=' ')

    print()
