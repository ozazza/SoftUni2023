# Input
a1 = int(input())
a2 = int(input())
n = int(input())

first = ''
second = 0
third = 0
forth = 0

# Logic
for f in range(a1, a2):

    if f % 2 != 0:
        first = chr(f)

        for s in range(1, n):
            second = s

            for t in range(1, int(n / 2)):
                third = t
                forth = f

                if (s + t + f) % 2 != 0:
                    print(f'{first}-{second}{third}{forth}')
