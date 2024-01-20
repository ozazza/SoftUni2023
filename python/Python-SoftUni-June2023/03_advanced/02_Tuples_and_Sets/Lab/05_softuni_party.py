n = int(input())
reservations = set()

for _ in range(n):
    reservations.add(input())

guest = ''
while True:
    if guest == 'END':
        break
    guest = input()

    if guest in reservations:
        reservations.remove(guest)

print(len(reservations))
for g in sorted(reservations):
    print(g)
