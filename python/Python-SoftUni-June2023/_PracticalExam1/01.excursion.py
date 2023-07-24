# Input
people = int(input())
nights = int(input())
cards = int(input())
tickets = int(input())

# Logic
unexpected_costs_percent = 1.25
price_nights = 20 * nights
price_cards = 1.60 * cards
price_tickets = 6 * tickets

costs = (price_nights + price_cards + price_tickets) * people
total = costs * unexpected_costs_percent

# Output
print(f'{total:.2f}')
