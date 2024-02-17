from collections import deque

money_stack = [int(x) for x in input().split(' ')]
prices = deque([int(x) for x in input().split(' ')])

count_food = 0
change = 0
while money_stack and prices:
    curr_money = money_stack[-1]
    curr_price = prices[0]

    if change > 0:
        curr_money += change
        change = 0

    if curr_money == curr_price:
        count_food += 1

    elif curr_money > curr_price:
        count_food += 1
        change = curr_money - curr_price

    money_stack.pop()
    prices.popleft()

if count_food >= 4:
    print(f'Gluttony of the day! Henry ate {count_food} foods.')
elif 1 < count_food < 4:
    print(f'Henry ate: {count_food} foods.')
elif count_food == 1:
    print(f'Henry ate: {count_food} food.')
else:
    print('Henry remained hungry. He will try next weekend again.')
