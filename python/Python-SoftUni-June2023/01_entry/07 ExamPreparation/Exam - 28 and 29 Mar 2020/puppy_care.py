# Input
bought = int(input())

# Logic
bought *= 1000

while True:
    eats = input()

    if eats == 'Adopted':
        break
    bought -= int(eats)

# Output
if bought >= 0:
    print(f'Food is enough! Leftovers: {bought} grams.')
else:
    print(f'Food is not enough. You need {abs(bought)} grams more.')
