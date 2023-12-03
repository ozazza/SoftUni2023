
def replace_substring(find_string: str, new_string: str, text: str) -> str:
    while find_string in text:
        text = text.replace(find_string, new_string)

    return text


spell = input()
result = ''
while True:
    command = input()
    if command == 'Abracadabra':
        break

    result = ''
    length = len(command.split())

    # Abjuration | Necromancy
    if length == 1:
        if command == 'Abjuration':

            result = spell.upper()
            print(result)
            spell = result

        elif command == 'Necromancy':
            result = spell.lower()
            print(result)
            spell = result
        else:
            print('The spell did not work!')

    # Alteration {substring}
    elif length == 2:
        potion, sub = command.split()

        if potion == 'Alteration' and sub in spell:
            result = replace_substring(sub, '', spell)
            print(result)
            spell = result
        else:
            print('The spell did not work!')

    # Illusion {index} {letter}" | Divination {first substring} {second substring}
    elif length == 3:
        comm1, comm2, comm3 = command.split()

        if comm1 == 'Illusion':
            index, letter = int(comm2), comm3

            if index < len(spell):
                for i in range(len(spell)):
                    if i == index:
                        result += letter
                    else:
                        result += spell[i]
                print('Done!')
                spell = result
            else:
                print('The spell was too weak.')

        elif comm1 == 'Divination':
            sub1, sub2 = comm2, comm3

            if sub1 in spell:
                result = replace_substring(sub1, sub2, spell)
                print(result)
                spell = result

        else:
            print('The spell did not work!')