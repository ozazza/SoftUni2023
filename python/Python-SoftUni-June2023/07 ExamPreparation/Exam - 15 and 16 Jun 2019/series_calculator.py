from math import floor

# Input
name = input()
seasons = int(input())
episodes = int(input())
episode_duration = float(input())
ads = 0.2
special = 10

# Logic

time_duration = seasons * episodes * (episode_duration + (episode_duration * ads))
special_duration = seasons * special
total_series_time = floor(time_duration + special_duration)

# Output
print(f'Total time needed to watch the {name} series is {total_series_time} minutes.')
