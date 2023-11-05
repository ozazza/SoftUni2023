happiness = input().split()
factor = int(input())

improvement = [int(x) * factor for x in happiness]
people = len(improvement)
average = sum(improvement) / people

people_happy = [p for p in improvement if p >= average]

if len(people_happy) >= people / 2:
    print(f'Score: {len(people_happy)}/{people}. Employees are happy!')
else:
    print(f'Score: {len(people_happy)}/{people}. Employees are not happy!')
