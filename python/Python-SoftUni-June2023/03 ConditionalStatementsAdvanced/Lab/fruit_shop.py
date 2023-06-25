# Input
fruit = input()
day = input()
qty = float(input())

fruits = ['banana', 'apple', 'orange', 'grapefruit', 'kiwi', 'pineapple', 'grapes']
price = 0
result = 0
output = 'error'

# Logic
if fruit in fruits:
    if day == 'Saturday' or day == 'Sunday':
        if fruit == 'banana':
            price = 2.7
        elif fruit == 'apple':
            price = 1.25
        elif fruit == 'orange':
            price = 0.9
        elif fruit == 'pineapple':
            price = 5.6
        elif fruit == 'grapefruit':
            price = 1.60
        elif fruit == 'kiwi':
            price = 3
        elif fruit == 'grapes':
            price = 4.2
    elif day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' or day == 'Thursday' or day == 'Friday':
        if fruit == 'banana':
            price = 2.5
        elif fruit == 'apple':
            price = 1.2
        elif fruit == 'orange':
            price = 0.85
        elif fruit == 'pineapple':
            price = 5.5
        elif fruit == 'grapefruit':
            price = 1.45
        elif fruit == 'kiwi':
            price = 2.7
        elif fruit == 'grapes':
            price = 3.85

# Output
if price > 0:
    result = price * qty
    print(f'{result:.2f}')
else:
    print(output)
