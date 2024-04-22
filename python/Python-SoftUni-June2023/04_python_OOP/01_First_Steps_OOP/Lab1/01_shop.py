class Shop:
    def __init__(self, name, items):
        self.name = name
        self.items = items

    def get_items_count(self):
        return len(self.items)


billa = Shop("Billa", ['apple', 'bread'])

print(billa.__dict__)
print(billa.get_items_count())