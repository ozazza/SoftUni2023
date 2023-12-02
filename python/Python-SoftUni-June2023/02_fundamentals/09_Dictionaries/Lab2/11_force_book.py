
def get_key_from_dict_value(text: str, dictionary: dict) -> str:
    for key, value in dictionary.items():
        for v in value:
            if v == text:
                return key
    return 'not found'


book = {}
while True:
    command = input()
    if command == 'Lumpawaroo':
        break

    side = ''
    user = ''

    if '|' in command:
        side, user = command.split(' | ')

        if side not in book.keys():
            book[side] = []
        if get_key_from_dict_value(user, book) == 'not found':
            book[side].append(user)

    elif '->' in command:
        user, side = command.split(' -> ')

        if side not in book.keys():
            book[side] = []

        if get_key_from_dict_value(user, book) != 'not found':
            book_key = get_key_from_dict_value(user, book)
            book[book_key].remove(user)

        if get_key_from_dict_value(user, book) == 'not found':
            book[side].append(user)

        print(f'{user} joins the {side} side!')

for key, values in book.items():
    if len(values) > 0:
        print(f'Side: {key}, Members: {len(values)}')

        for person in values:
            print(f'! {person}')
