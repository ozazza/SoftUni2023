fire_type = input().split('#')
water_needed = int(input())

effort = 0.0
total_fire = 0

print('Cells:')

for i in fire_type:
    fire = i.split(' = ')
    water = int(fire[1])
    type_f = fire[0]

    high_fire = type_f == 'High' and (81 <= water <= 125)
    mid_fire = type_f == 'Medium' and (51 <= water <= 80)
    low_fire = type_f == 'Low' and (1 <= water <= 50)

    if water_needed >= water and (high_fire or mid_fire or low_fire):
        water_needed -= water
        effort += water * 0.25
        total_fire += water

        print(f' - {water}')

print(f'Effort: {effort:.2f}')
print(f'Total Fire: {total_fire}')
