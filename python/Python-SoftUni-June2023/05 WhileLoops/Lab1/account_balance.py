# Logic
command_break = 'NoMoreMoney'
amount = 0

while True:
    user_input = input()

    if user_input == command_break:
        break

    if float(user_input) < 0:
        print('Invalid operation!')
        break

    print(f'Increase: {float(user_input):.2f}')
    amount += float(user_input)

# Output
print(f'Total: {amount:.2f}')
