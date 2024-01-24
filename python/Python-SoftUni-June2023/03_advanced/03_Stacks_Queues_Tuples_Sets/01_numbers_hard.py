first_set = set(int(x) for x in input().split())
second_set = set(int(x) for x in input().split())

functions = {
    'Add First': lambda x: [first_set.add(int(el)) for el in x], # or first_set.update(second_set)
    'Add Second': lambda x: [second_set.add(int(el)) for el in x],
    'Remove First': lambda x: [first_set.discard(int(el)) for el in x],
    'Remove Second': lambda x:  [second_set.discard(int(el)) for el in x],
    'Check Subset': lambda x: print(first_set.issubset(second_set) or second_set.issubset(first_set)),
}


for _ in range(int(input())):
    # "Add First 1 2 3" -> ['Add', 'First', '1', '2', '3']
    first_command, second_command, *data = input().split()  # The * sign means Pack all left

    command = first_command + ' ' + second_command

    functions[command](data)

print(*sorted(first_set), sep=', ')
print(*sorted(second_set), sep=', ')
