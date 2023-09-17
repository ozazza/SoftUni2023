# Input
budget = float(input())
gpus = int(input())
cpus = int(input())
rams = int(input())

# Logic
gpu_price = 250 * gpus
cpu_price = gpu_price * 0.35 * cpus
ram_price = gpu_price * 0.1 * rams
discount = 0.15

amount = gpu_price + cpu_price + ram_price

if gpus > cpus:
    amount -= amount * discount

budget_left = abs(budget - amount)

# Output
if budget >= amount:
    print(f'You have {budget_left:.2f} leva left!')
else:
    print(f'Not enough money! You need {budget_left:.2f} leva more!')
