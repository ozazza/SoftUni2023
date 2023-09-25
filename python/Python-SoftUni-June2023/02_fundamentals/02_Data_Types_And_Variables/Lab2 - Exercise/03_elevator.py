people = int(input())
capacity = int(input())

courses = int(people / capacity)
left_people = people % capacity

if left_people > 0:
    courses += 1

print(courses)
