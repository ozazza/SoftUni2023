# Input
age = float(input())
gender = input()

result = ''

# Logic
if age >= 16:
    if gender == 'm':
        result = 'Mr.'
    elif gender == 'f':
        result = 'Ms.'
else:
    if gender == 'm':
        result = 'Master'
    elif gender == 'f':
        result = 'Miss'

# Output
print(result)
