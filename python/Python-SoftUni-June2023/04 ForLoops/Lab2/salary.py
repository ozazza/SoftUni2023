# Input
tabs_count = int(input())
salary = int(input())

facebook_penalty = 150
instagram_penalty = 100
reddit_penalty = 50
total_penalty = 0
is_lost = False

# Logic
for i in range(tabs_count):
    site = input()

    if site == 'Facebook':
        total_penalty += facebook_penalty
    elif site == 'Instagram':
        total_penalty += instagram_penalty
    elif site == 'Reddit':
        total_penalty += reddit_penalty

    if salary <= total_penalty:
        is_lost = True
        break

# Output
if is_lost:
    print('You have lost your salary.')
else:
    print(salary - total_penalty)
