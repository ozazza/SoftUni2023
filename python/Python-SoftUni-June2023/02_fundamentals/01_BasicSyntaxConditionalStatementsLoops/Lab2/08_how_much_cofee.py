coffee_count = 0
while True:
    command = input()
    if command == 'END':
        break
    elif command.lower() == 'dog' or command.lower() == 'cat' or command.lower() == 'coding' or command.lower() == 'movie':

        first_char = command[0]
        if first_char.isupper():
            coffee_count += 2
        else:
            coffee_count += 1

if coffee_count > 5:
    print('You need extra sleep')
else:
    print(coffee_count)
