from collections import deque

customers = deque()
while True:
    command = input()
    if command == "End":
        break

    if command == "Paid":
        while customers:
            print(customers.popleft())
    else:
        customers.append(command)

print(f'{len(customers)} people remaining.')
