# Input
name = input()
academy_points = float(input())
jury = int(input())

target_oscar = 1250.5
total_points = academy_points
is_nominated = False

# Logic
for i in range(jury):
    reviewer_name = input()
    reviewer_points = float(input())

    total_points += len(reviewer_name) * reviewer_points / 2

    if total_points >= target_oscar:
        is_nominated = True
        break

# Output
if is_nominated:
    print(f'Congratulations, {name} got a nominee for leading role with {total_points:.1f}!')
else:
    print(f'Sorry, {name} you need {(target_oscar - total_points):.1f} more!')
