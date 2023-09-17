# Input
product = input()

type_product = 'unknown'

# Logic
if product == 'banana' or product == 'apple' or product == 'kiwi' or product == 'cherry' or product == 'lemon' or product == 'grapes':
    type_product = 'fruit'
elif product == 'tomato' or product == 'cucumber' or product == 'pepper' or product == 'carrot':
    type_product = 'vegetable'

# Output
print(type_product)
