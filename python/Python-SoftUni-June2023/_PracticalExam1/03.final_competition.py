# Input
dancers = int(input())
points = float(input())
season = input()
place = input()

# Logic
amount = dancers * points
reward_abroad = 1.5
expenses = 0

if place == 'Bulgaria':
    if season == 'summer':
        expenses = 0.05 * amount
    elif season == 'winter':
        expenses = 0.08 * amount
if place == 'Abroad':
    amount *= reward_abroad
    if season == 'summer':
        expenses = 0.1 * amount
    elif season == 'winter':
        expenses = 0.15 * amount

total_amount = amount - expenses
charity = 0.75 * total_amount
amount_left = total_amount - charity
amount_per_person = amount_left / dancers

# Output
print(f'Charity - {charity:.2f}')
print(f'Money per dancer - {amount_per_person:.2f}')
