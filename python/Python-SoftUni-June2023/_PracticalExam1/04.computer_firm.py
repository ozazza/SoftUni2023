# Input
computers = int(input())

# Logic
total_sales = 0
total_rating = 0
ave_rating = 0

for pc in range(computers):
    sales_rate = int(input())
    sales_percent = 0

    possible_sales = sales_rate // 10
    rate = sales_rate % (possible_sales * 10)

    if rate == 3:
        sales_percent = 0.5
    elif rate == 4:
        sales_percent = 0.7
    elif rate == 5:
        sales_percent = 0.85
    elif rate == 6:
        sales_percent = 1

    total_sales += sales_percent * possible_sales
    total_rating += rate

ave_rating = total_rating / computers

# Output
print(f'{total_sales:.2f}')
print(f'{ave_rating:.2f}')
