# Logic
command_break = 'Stop'
max_number = 0

while True:
    user_input = input()

    if user_input == command_break:
        break

    number = int(user_input)
    old_number = number
