phonebook = {}
search_people = 0
while True:

    person = input()

    if '-' not in person:
        search_people = int(person)
        break

    entry = person.split('-')
    phonebook[entry[0]] = entry[1]

for i in range(search_people):
    search_name = input()
    if search_name in phonebook.keys():
        print(f'{search_name} -> {phonebook[search_name]}')
    else:
        print(f'Contact {search_name} does not exist.')
