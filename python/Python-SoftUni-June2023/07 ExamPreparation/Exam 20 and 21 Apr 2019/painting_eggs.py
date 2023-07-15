# Input
size = input()
color = input()
qty = int(input())

# Logic
price = 0
total_price = 0
if size == 'Large':
    if color == 'Red':
        price = 16
    elif color == 'Green':
        price = 12
    elif color == 'Yellow':
        price = 9
elif size == 'Medium':
    if color == 'Red':
        price = 13
    elif color == 'Green':
        price = 9
    elif color == 'Yellow':
        price = 7
elif size == 'Small':
    if color == 'Red':
        price = 9
    elif color == 'Green':
        price = 8
    elif color == 'Yellow':
        price = 5

price *= qty
discount = price * 0.35
total_price = price - discount

# Output
print(f'{total_price:.2f} leva.')
