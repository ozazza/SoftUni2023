# Input
num = int(input())

# Logic - reads number backward
first_digit = num % 10
second_digit = num % 100 // 10
last_digit = num // 100

for first in range(1, first_digit + 1):
    if first > 0:
        for second in range(1, second_digit + 1):
            if second > 0:
                for last in range(1, last_digit + 1):
                    if last > 0:
                        print(f'{first} * {second} * {last} = {first * second * last};')
