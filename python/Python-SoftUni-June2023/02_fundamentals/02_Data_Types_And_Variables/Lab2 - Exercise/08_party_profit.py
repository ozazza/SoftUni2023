group = int(input())
days = int(input())

earned = 0
for day in range(1, days + 1):

    if day % 10 == 0:
        group -= 2
    if day % 15 == 0:
        group += 5

    earned += 50 - (group * 2)

    if day % 3 == 0:
        earned -= group * 3

    if day % 5 == 0:
        earned += group * 20

        if day % 3 == 0:
            earned -= (group * 2)

coins_companion = int(earned / group)
print(f'{group} companions received {coins_companion} coins each.')
