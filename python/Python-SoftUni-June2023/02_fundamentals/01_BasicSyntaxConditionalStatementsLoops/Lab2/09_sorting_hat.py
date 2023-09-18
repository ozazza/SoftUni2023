
while True:
    name = input()

    if name == 'Welcome!':
        print('Welcome to Hogwarts.')
        break
    elif name == 'Voldemort':
        print('You must not speak of that name!')
        break
    else:
        name_len = len(name)
        if name_len < 5:
            house = 'Gryffindor'
        elif name_len == 5:
            house = 'Slytherin'
        elif name_len == 6:
            house = 'Ravenclaw'
        elif name_len > 6:
            house = 'Hufflepuff'

        print(f'{name} goes to {house}.')
