# Logic
command_break = 'Stop'
max_number = int(input())

while True:
    user_input = input()

    if user_input == command_break:
        break

    number = int(user_input)
    if number > max_number:
        max_number = number

# Output
print(max_number)
