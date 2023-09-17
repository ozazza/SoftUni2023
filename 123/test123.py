# Input
user_number = int(input())

# Logic
for i in range(user_number + 1):
    for j in range(i + 1, user_number):
        print(j, end=' ')

    print()