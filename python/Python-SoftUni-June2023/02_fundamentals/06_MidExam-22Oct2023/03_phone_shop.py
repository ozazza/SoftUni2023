storage = input().split(', ')

command = ''
while True:
    order = input().split(' - ')
    command = order[0]

    if command == 'End':
        break

    else:
        phone = order[1]
        if command == 'Add':
            if phone not in storage:
                storage.append(phone)

        elif command == 'Remove':
            if phone in storage:
                storage.pop(storage.index(phone))

        elif command == 'Bonus phone':
            ph = phone.split(':')
            old_phone = ph[0]
            new_phone = ph[1]
            if old_phone in storage:
                storage.append(new_phone)
                index_new = storage.index(storage[-1])
                index_next_old = storage.index(old_phone) + 1
                storage[index_next_old], storage[index_new] = storage[index_new], storage[index_next_old]
        elif command == 'Last':
            if phone in storage:
                storage.remove(phone)
                storage.append(phone)

print(', '.join([x for x in storage]))
