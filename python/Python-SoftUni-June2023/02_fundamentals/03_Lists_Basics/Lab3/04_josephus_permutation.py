people = input().split(' ')
k = int(input())

counter = 0
i = 0
executed = list()
while len(people) > 0:
    counter += 1

    if counter % k == 0:
        # print(people[i], end=' ')
        executed.append(people[i])
        people.pop(i)
    else:

        i += 1

    if i >= len(people):
        i = 0

prt_str = ','.join([str(x) for x in executed.copy()])
print(f'[{prt_str}]')
