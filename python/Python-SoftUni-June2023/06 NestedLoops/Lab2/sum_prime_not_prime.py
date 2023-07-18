# Logic
is_end = False
sum_non_primes = 0
sum_primes = 0

command = input()
while command != 'stop':

    if command == 'stop':
        is_end = True
        break

    user_number = int(command)
    if user_number < 0:
        print('Number is negative.')
        command = input()
        continue

    is_prime = True
    for number in range(2, user_number):
        if user_number % number == 0:
            is_prime = False
            break

    if is_prime:
        sum_primes += user_number
    else:
        sum_non_primes += user_number

    command = input()

# Output
print(f'Sum of all prime numbers is: {sum_primes}')
print(f'Sum of all non prime numbers is: {sum_non_primes}')
