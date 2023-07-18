# Input
number = int(input())

# Logic
counter = 0
for a in range(number + 1):
    for b in range(number + 1):
        for c in range(number + 1):
            if a + b + c == number:
                counter += 1

# Output
print(counter)
