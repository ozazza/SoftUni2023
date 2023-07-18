# Input
min_number = int(input())

# Logic
command_break = 'Stop'

while True:
    user_input = input()

    if user_input == command_break:
        break

    number = int(user_input)

    if number < min_number:
        min_number = number

# Output
print(min_number)
