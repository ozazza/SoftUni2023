given_cards = input().split(' ')
a = 11
b = 11

is_terminated = False
a_team_sent_off = list()
b_team_sent_off = list()

if len(given_cards) > 0:
    for card in given_cards:
        players = card.split('-')

        is_terminated = False
        if 'A' in card and players[1] not in a_team_sent_off:
            a -= 1
            a_team_sent_off.append(players[1])

        elif 'B' in card and players[1] not in b_team_sent_off:
            b -= 1
            b_team_sent_off.append(players[1])

        else:
            continue

        if a < 7 or b < 7:
            is_terminated = True
            break

print(f'Team A - {a}; Team B - {b}')

if is_terminated:
    print('Game was terminated')
