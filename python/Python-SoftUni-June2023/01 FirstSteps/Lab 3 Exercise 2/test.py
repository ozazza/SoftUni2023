from math import ceil

# user input
movie_name = input()
episode_length = int(input())
break_length = int(input())

# calculating breaks
lunch_time = break_length * 0.125
time_for_break = break_length * 0.25

# calculation of free time
remaining_time = break_length - time_for_break - lunch_time
time_left = ceil(abs(episode_length - remaining_time))

# logic
if remaining_time >= episode_length:
    print(f'You have enough time to watch {movie_name} and left with {time_left} minutes free time.')
else:
    print(f'You don\'t have enough time to watch {movie_name}, you need {time_left} more minutes.')
