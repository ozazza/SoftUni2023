cards = input().split()
shuffles = int(input())

deck = list()
deck_half_1 = list()
deck_half_2 = list()
half_deck_len = int((len(cards) - 1) / 2)

for s in range(shuffles):
    for card in range(len(cards)):
        if card <= half_deck_len:
            deck_half_1.append(cards[card])
        else:
            deck_half_2.append(cards[card])

    for i in range(half_deck_len + 1):
        deck.append(deck_half_1[i])
        deck.append(deck_half_2[i])

    cards = deck.copy()
    deck = list()
    deck_half_1 = list()
    deck_half_2 = list()

print(cards)
