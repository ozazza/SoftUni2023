budget = int(input())
total = 0

while True:
    command = input()
    if command != 'End':

        price = int(command)
        total = total + price

        if total > budget:
            print('You went in overdraft!')
            break
    else:
        print('You bought everything needed.')
        break
