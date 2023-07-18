# Read user input
number_of_juniors = int(input())
number_of_seniors = int(input())
type_of_trace = input()

# Logic
price_for_junior = 0
price_for_senior = 0
total_sum = 0
discount = 0
tax = 0

if type_of_trace == 'trail':
    price_for_junior = 5.50
    price_for_senior = 7
    # discount = total_sum * 0.05
elif type_of_trace == 'cross-country':
    price_for_junior = 8
    price_for_senior = 9.50
    # discount = total_sum * 0.05
elif type_of_trace == 'downhill':
    price_for_junior = 12.25
    price_for_senior = 13.75
    # discount = total_sum * 0.05
elif type_of_trace == 'road':
    price_for_junior = 20
    price_for_senior = 21.50
    # discount = total_sum * 0.05

total_sum = (number_of_juniors * price_for_junior) + (number_of_seniors * price_for_senior)
tax = total_sum * 0.05

if number_of_juniors + number_of_seniors >= 50:
    if type_of_trace == 'cross-country':
        discount = total_sum * 0.25

#     else:
#         discount = total_sum * 0.05
# else:
#   discount = total_sum * 0.05

final_price = total_sum - discount - tax

# Print output
print(f'{final_price:.2f}')