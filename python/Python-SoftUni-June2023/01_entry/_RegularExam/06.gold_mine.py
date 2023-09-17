# Input
locations = int(input())

# Logic
for i in range(locations):
    expected_extraction_day = float(input())
    days = int(input())

    location_extracted = 0
    location_ave_day = 0
    for day in range(days):
        extracted = float(input())
        location_extracted += extracted

    location_ave_day = location_extracted / days
    difference = location_ave_day - expected_extraction_day

    if difference >= 0:
        print(f'Good job! Average gold per day: {location_ave_day:.2f}.')
    else:
        print(f'You need {abs(difference):.2f} gold.')
