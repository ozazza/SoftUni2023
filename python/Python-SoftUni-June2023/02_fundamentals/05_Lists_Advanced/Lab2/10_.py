
def update_list_values(my_lst, new_value: int) -> list:

    for v in range(my_lst):
        if 0 < my_lst[v] <= new_value:
            my_lst[v] += new_value
        else:
            my_lst[v] += new_value

    return my_lst


distances = input().split()
distances = [int(m) for m in distances]
sum_removed = 0

while len(distances) > 0:
    inx = int(input())
    
    first_i = 0
    last_i = len(distances) - 1
    new_dist = []
    removed = 0

    if 0 <= inx < len(distances):
        removed = distances[inx]

        if inx == first_i:
            new_dist = distances[1:]

        elif inx == last_i:
            new_dist = distances[:inx]

        elif first_i < inx < last_i:
            new_dist = distances[:inx]
            new_dist += distances[inx + 1:]
    else:
        new_dist = distances
        if inx < 0:
            removed = new_dist[first_i]
            new_dist.pop(first_i)
            new_dist.insert(first_i, new_dist[last_i])

        elif inx > last_i:
            removed = new_dist[last_i]
            new_dist.pop()
            new_dist.append(new_dist[first_i])

    new_dist = update_list_values(new_dist, removed)

    sum_removed += removed
    distances = new_dist.copy()

print(sum_removed)

# 4 5 3 8 1 2
