# Input
breads = int(input())

# Logic
best_baker = ''
best_score = 0

for bread in range(breads):
    baker = input()
    score = ''
    baker_points = 0

    while True:
        score = input()

        if score == 'Stop':
            print(f'{baker} has {baker_points} points.')

            if baker_points > best_score:
                print(f'{baker} is the new number 1!')

            break

        baker_points += int(score)

    if baker_points > best_score:
        best_baker = baker
        best_score = baker_points

# Output
print(f'{best_baker} won competition with {best_score} points!')
