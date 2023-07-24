# Input
tshirt = float(input())
amount_to_reach = float(input())

# Logic
shorts = tshirt * 0.75
socks = shorts * 0.2
buttons = (tshirt + shorts) * 2
discount_percent = 0.15

amount = tshirt + shorts + socks + buttons
discount = amount * discount_percent
total_amount = amount - discount

difference = total_amount - amount_to_reach

# Output
if difference >= 0:
    print(f'Yes, he will earn the world-cup replica ball!')
    print(f'His sum is {total_amount:.2f} lv.')
else:
    print(f'No, he will not earn the world-cup replica ball.')
    print(f'He needs {abs(difference):.2f} lv. more.')
