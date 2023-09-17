# Input
n = int(input())
m = int(input())
s = int(input())

# Logic and Output
for i in range(m, n - 1, -1):
    if i % 2 == 0 and i % 3 == 0:
        if i == s:
            break

        print(i, end=' ')
