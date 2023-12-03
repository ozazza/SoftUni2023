heroes = {}

while True:
    command = input()
    if command == 'End':
        break

    if len(command.split()) == 2:
        task, hero = command.split()

        if task == 'Enroll':
            if hero not in heroes.keys():
                heroes[hero] = []
                # heroes[hero].append(hero)
            else:
                print(f'{hero} is already enrolled.')

    elif len(command.split()) == 3:
        task, hero, spell = command.split()

        if hero not in heroes.keys():
            print(f'{hero} doesn\'t exist.')
            continue

        if task == 'Learn':

            if spell in heroes[hero]:
                print(f'{hero} has already learnt {spell}.')
                continue

            heroes[hero].append(spell)

        elif task == 'Unlearn':

            if spell not in heroes[hero]:
                print(f'{hero} doesn\'t know {spell}.')
                continue

            heroes[hero].remove(spell)

print('Heroes:')
for h, s in heroes.items():
    hero_spells = ', '.join(heroes[h])
    print(f'== {h}: {hero_spells}')
