degrees = float(input())

weather = 'unknown'
if 26 <= degrees <= 35:
    weather = 'Hot'
elif 20.1 <= degrees <= 25.9:
    weather = 'Warm'
elif 15 <= degrees <= 20:
    weather = 'Mild'
elif 12 <= degrees <= 14.9:
    weather = 'Cool'
elif 5 <= degrees <= 11.9:
    weather = 'Cold'

print(weather)
