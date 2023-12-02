num_commands = int(input())
park = {}

for n in range(num_commands):
    command = input().split()
    name = command[1]

    if command[0] == 'register':
        plate = command[2]
        if name not in park.keys():
            park[name] = plate
            print(f'{name} registered {plate} successfully')
        else:
            print(f'ERROR: already registered with plate number {plate}')
    elif command[0] == 'unregister':
        if name not in park.keys():
            print(f'ERROR: user {name} not found')
        else:
            leaving_car_plate = park.pop(name)
            print(f'{name} unregistered successfully')

for k, v in park.items():
    print(f'{k} => {v}')
