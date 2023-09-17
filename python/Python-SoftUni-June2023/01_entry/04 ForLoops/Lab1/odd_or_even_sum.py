# Input
n = int(input())

# Logic
odd_sum = 0
even_sum = 0
number = 0

for i in range(1, n + 1):
    number = int(input())
    if i % 2 == 0:
        even_sum += number
    else:
        odd_sum += number

# Output
if even_sum == odd_sum:
    print('Yes')
    print(f'Sum = {even_sum}')
else:
    print(f'No')
    print(f'Diff = {abs(even_sum - odd_sum)}')
