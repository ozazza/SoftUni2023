# Input
number = int(input())

result = ''
is_valid = (99 < number < 201) or number == 0

# Logic
if not is_valid:
    result = 'invalid'

# Output
print(result)
