events = input().split('|')

coins = 100
energy = 100

is_completed = True
for event in events:
    e = event.split('-')

    if e[0] == 'rest':

        gained = int(e[1])

        if gained + energy > 100:
            gained = 100 - energy

        energy += gained
        print(f'You gained {gained} energy.')
        print(f'Current energy: {energy}.')

    elif e[0] == 'order':
        if energy >= 30:
            energy -= 30
            coins += int(e[1])
            print(f'You earned {e[1]} coins.')
        else:
            energy += 50
            print(f'You had to rest!')
    else:
        if coins >= int(e[1]):
            coins -= int(e[1])
            print(f'You bought {e[0]}.')
        else:
            print(f'Closed! Cannot afford {e[0]}.')
            is_completed = False
            break

if is_completed:
    print('Day completed!')
    print(f'Coins: {coins}')
    print(f'Energy: {energy}')
