from math import floor

# Input
tournaments = int(input())
rank_points = int(input())

winner = 2000
final = 1200
semi = 720
season_points = 0
average_points = 0
total_points = 0
wins_count = 0

# Logic
for tour in range(tournaments):
    position = input()

    if position == 'W':
        season_points += winner
        wins_count += 1
    if position == 'F':
        season_points += final
    if position == 'SF':
        season_points += semi

average_points = season_points / tournaments
total_points += season_points + rank_points

# Output
print(f'Final points: {total_points}')
print(f'Average points: {floor(average_points)}')
print(f'{(wins_count / tournaments) * 100:.2f}%')
