days = int(input())
players = int(input())
group_energy = float(input())
water_person_day = float(input())
food_person_day = float(input())

group_water = water_person_day * days * players
group_food = food_person_day * days * players
energy_lost = 0.0
for day in range(1, days + 1):

    energy_lost = float(input())
    group_energy -= energy_lost

    if group_energy <= 0:
        print(f'You will run out of energy. You will be left with {group_food:.2f} food and {group_water:.2f} water.')
        break

    if day % 2 == 0:
        group_water -= group_water * 0.3
        group_energy += group_energy * 0.05

    if day % 3 == 0:
        group_food -= group_food / players
        group_energy += group_energy * 0.1

if group_energy > 0:
    print(f'You are ready for the quest. You will be left with - {group_energy:.2f} energy!')
