budget = float(input())
flour_kg_price = float(input())

pack_eggs_price = 0.75 * flour_kg_price
milk_l_price = 1.25 * flour_kg_price

loaves = 0
colored_eggs = 0

loaf_price = pack_eggs_price + flour_kg_price + (milk_l_price / 4)
money_left = budget

while money_left >= loaf_price:
    # total_price = pack_eggs_price + flour_kg_price

    total_price = loaf_price
    # if loaves % 4 == 0:
    #
    #     # check left price
    #     if budget >= milk_l_price:
    #         total_price += milk_l_price
    #     else:
    #         break

    loaves += 1
    colored_eggs += 3

    if loaves % 3 == 0:
        colored_eggs -= loaves - 2

    money_left -= total_price

print(f'You made {loaves} loaves of Easter bread! Now you have {colored_eggs} eggs and {money_left:.2f}BGN left.')
