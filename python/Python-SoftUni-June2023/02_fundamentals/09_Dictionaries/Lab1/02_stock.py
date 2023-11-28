elements = input().split()
store = dict()

for i in range(0, len(elements), 2):
    key = elements[i]
    value = elements[i + 1]
    store[key] = int(value)

find_products = input().split()

for p in find_products:
    if p in store:
        print(f"We have {store[p]} of {p} left")
    else:
        print(f"Sorry, we don't have {p}")
