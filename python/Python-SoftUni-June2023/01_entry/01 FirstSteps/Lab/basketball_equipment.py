year_tax = int(input())

sneakers = year_tax - (year_tax * 0.4)
training_suit = sneakers - (sneakers * 0.2)
ball = training_suit * 0.25
accessories = ball * 0.2

expenses = year_tax + sneakers + training_suit + ball + accessories

print(expenses)
