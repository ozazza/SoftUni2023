# Input
n = int(input())

# Logic
sum_numbers = 0
max_element = 0

for i in range(n):
    number = int(input())

    if max_element < number:
        max_element = number

    sum_numbers += number

diff = abs(sum_numbers - max_element - max_element)

# Output
if max_element == sum_numbers - max_element:
    print('Yes')
    print(f'Sum = {max_element}')
else:
    print('No')
    print(f'Diff = {abs(diff)}')
