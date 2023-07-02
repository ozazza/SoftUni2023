# Input
n = int(input())

n_max = 0
n_min = 0

# Logic
for i in range(n):
    number = int(input())

    if i == 0:
        n_max = number
        n_min = number

    if number < n_min:
        n_min = number

    if number > n_max:
        n_max = number

# Output
print(f'Max number: {n_max}')
print(f'Min number: {n_min}')
