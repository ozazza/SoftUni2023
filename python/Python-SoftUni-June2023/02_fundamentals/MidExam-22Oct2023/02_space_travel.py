route = input().split('||')
fuel = int(input())
ammo = int(input())

is_failed = False
for i in route:

    if 'Titan' in i:
        print('You have reached Titan, all passengers are safe.')
    else:
        unit = i.split(' ')
        unit_type = unit[0]
        unit_val = int(unit[1])
        if unit_type == 'Travel':
            if 0 < fuel >= unit_val:
                print(f'The spaceship travelled {unit_val} light-years.')
            else:
                is_failed = True
                break

        elif unit_type == 'Enemy':
            if ammo >= unit_val:
                ammo -= unit_val
                print(f'An enemy with {unit_val} armour is defeated.')
            elif ammo < unit_val and fuel >= unit_val * 2:
                fuel -= unit_val * 2
                print(f'An enemy with {unit_val} armour is outmaneuvered.')
            else:
                is_failed = True
                break

        elif unit_type == 'Repair':
            fuel += unit_val
            ammo += unit_val * 2
            print(f'Ammunitions added: {unit_val * 2}.')
            print(f'Fuel added: {unit_val}.')

if is_failed:
    print('Mission failed.')
