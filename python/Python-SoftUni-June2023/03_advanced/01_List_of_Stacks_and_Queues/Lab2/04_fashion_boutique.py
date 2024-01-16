box = [int(x) for x in input().split()]
rack_max = int(input())

racks = 1
rack_capacity = 0
while box:
    item = box.pop()
    if rack_capacity + item <= rack_max:
        rack_capacity += item
    else:
        racks += 1
        rack_capacity = item

print(racks)
