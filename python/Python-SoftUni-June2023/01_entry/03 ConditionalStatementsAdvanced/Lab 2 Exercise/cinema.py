# Input
type_projection = input()
rows = int(input())
cols = int(input())

premiere_price = 12
normal_price = 7.5
discount_price = 5

result = rows * cols

# Logic
if type_projection == 'Premiere':
    result *= premiere_price
elif type_projection == 'Normal':
    result *= normal_price
elif type_projection == 'Discount':
    result *= discount_price

# Output
print(f'{result:.2f} leva')
