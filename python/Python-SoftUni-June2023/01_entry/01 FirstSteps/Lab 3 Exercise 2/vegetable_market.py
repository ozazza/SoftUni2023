price_vegetables = float(input())
price_fruits = float(input())
kg_vegetables = float(input())
kg_fruits = float(input())

eur = 1.94
amt_vegetables = price_vegetables * kg_vegetables
amt_fruits = price_fruits * kg_fruits
amt_total_bgn = amt_vegetables + amt_fruits
amt_total_eur = amt_total_bgn / eur

print(f'{amt_total_eur:.2f}')
