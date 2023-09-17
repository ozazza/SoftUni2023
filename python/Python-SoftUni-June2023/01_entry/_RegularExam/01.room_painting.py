from math import ceil
from math import floor

# Input
paint = int(input())
wallpapers = int(input())
gloves_pair_price = float(input())
paintbrush_price = float(input())

# Logic
paint_price = 21.5 * paint
wallpapers_price = 5.2 * wallpapers
gloves_price = ceil(wallpapers * 0.35) * gloves_pair_price
paintbrushes_price = floor(paint * 0.48) * paintbrush_price

total_price = paint_price + wallpapers_price + gloves_price + paintbrushes_price
delivery = total_price / 15

# Output
print(f'This delivery will cost {delivery:.2f} lv.')
