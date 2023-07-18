# Read user input
days = int(input())
type_room = input()
rating = input()

nights = days - 1
price_per_night = 0

# Logic
if type_room == 'president apartment':
    price_per_night = 35
    if nights < 10:
        price_per_night *= 0.9
    elif nights <= 15:
        price_per_night *= 0.85
    elif nights > 15:
        price_per_night *= 0.8
elif type_room == 'apartment':
    price_per_night = 25
    if nights < 10:
        price_per_night *= 0.7
    elif nights <= 15:
        price_per_night *= 0.65
    elif nights > 15:
        price_per_night *= 0.5
elif type_room == 'room for one person':
    price_per_night = 18

total_sum = nights * price_per_night

if rating == 'positive':
    total_sum *= 1.25
elif rating == 'negative':
    total_sum *= 0.9

# Print output
print(f'{total_sum:.2f}')
