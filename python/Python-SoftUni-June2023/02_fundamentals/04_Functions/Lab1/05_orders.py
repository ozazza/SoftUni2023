def calculate_total_price(product_type: str, qty: float):
    price = 0.0
    if product_type == 'coffee':
        price = 1.5
    if product_type == 'coke':
        price = 1.4
    if product_type == 'water':
        price = 1.0
    if product_type == 'snacks':
        price = 2.0

    total = qty * price

    return f'{total:.2f}'


product = input()
n = float(input())

result = calculate_total_price(product, n)

print(result)
