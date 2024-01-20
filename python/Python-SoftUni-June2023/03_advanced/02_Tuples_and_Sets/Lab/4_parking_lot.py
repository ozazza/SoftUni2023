n = int(input())

parking = set()
for _ in range(n):
    direction, plate = input().split(', ')

    if direction == 'IN':
        parking.add(plate)
    else:
        parking.remove(plate)

if parking:
    for car in parking:
        print(car)
else:
    print('Parking Lot is Empty')
