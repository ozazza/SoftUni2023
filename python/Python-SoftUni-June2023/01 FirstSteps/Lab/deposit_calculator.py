
deposit_sum = float(input())
deposit_months = int(input())
annual_interest_rate = float(input()) / 100

amount = deposit_sum + deposit_months * ((deposit_sum * annual_interest_rate) / 12)

print(amount)