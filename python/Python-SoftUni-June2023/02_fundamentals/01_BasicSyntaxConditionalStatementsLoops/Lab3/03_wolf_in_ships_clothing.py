animals = input().split(', ')

last_before_me = len(animals) - 1
wolf_position = animals.index('wolf')

if wolf_position is last_before_me:
    print('Please go away and stop eating my sheep')
else:
    animals.reverse()
    sheep_in_danger = animals.index('wolf')

    print(f'Oi! Sheep number {sheep_in_danger}! You are about to be eaten by a wolf!')
