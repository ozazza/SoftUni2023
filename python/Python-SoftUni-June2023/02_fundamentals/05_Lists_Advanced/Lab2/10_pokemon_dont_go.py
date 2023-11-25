distances = input().split(' ')

while True:
    inx = int(input())

    if inx == 0:
        new_dist = distances[1:]

    elif inx == distances[-1]:
        new_dist = distances[:inx - 1]

    elif 0 < inx < len(distances) - 1:
        new_dist = distances[:inx - 1]
        new_dist.append(' '.join(distances[inx + 1:]))
    break
print(distances)
