class Catalogue:
    def __init__(self, name: str):
        self.name = name
        self.products = []

    def add_product(self, product_name: str):
        self.products.append(product_name)

    def get_by_letter(self, first_letter: str):
        target_products = []
        for product in self.products:
            if product[0] == first_letter:
                target_products.append(product)

        return target_products

    def __repr__(self):
        result = f"Items in the {self.name} catalogue:"
        for p in sorted(self.products, reverse=False):
            result += f"\n{p}"

        return result


catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)
