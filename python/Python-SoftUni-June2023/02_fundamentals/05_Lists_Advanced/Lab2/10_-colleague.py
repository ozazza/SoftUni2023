distance = [int(number) for number in input().split()]
total_result = 0


def update_list(lst, value: int) -> list:
    for current_idx in range(0, len(lst)):
        if lst[current_idx] <= result:
            lst[current_idx] += result
        else:
            lst[current_idx] -= result

    return lst


while True:
    if len(distance) <= 0:
        break
    index = int(input())
    result = 0
    if index < 0:
        result += distance[0]

        distance = update_list(distance, result)

        distance.pop(0)
        distance.insert(0, distance[-1])

    elif index > len(distance) - 1:
        result += distance[-1]

        distance = update_list(distance, result)

        distance.pop()
        distance.insert(distance[-1], distance[0])
    if index in range(0, len(distance)):
        result += distance[index]

        distance = update_list(distance, result)

        distance.pop(index)
    total_result += result
print(total_result)