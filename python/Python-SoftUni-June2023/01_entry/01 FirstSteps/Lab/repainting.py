shield_sq_m = int(input())
paint_lit = int(input())
chems_lit = int(input())
hours_work = int(input())

shield = (shield_sq_m + 2) * 1.5
paint = (paint_lit + (0.1 * paint_lit)) * 14.5
chems = chems_lit * 5
bags = 0.40

materials = shield + paint + chems + bags
labor = hours_work * materials * 0.3
expenses = materials + labor

print(expenses)