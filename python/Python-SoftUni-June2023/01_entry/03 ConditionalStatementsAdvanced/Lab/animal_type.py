# Input
animal = input()
result = 'unknown'

# Logic
if animal == 'dog':
    result = 'mammal'
elif animal == 'crocodile' or animal == 'tortoise' or animal == 'snake':
    result = 'reptile'

# Output
print(result)