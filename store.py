from products import Product

class Store:
    """
    This module defines the Store class.
    It manages a list of Product instances and allows adding/removing products.
    It can calculate total quantity and process multi-product orders.
    """

    def __init__(self, products=None):
        if products is None:
            products = []
        self.products = products

    def add_product(self, product):
        if isinstance(product, Product):
            self.products.append(product)
        else:
            raise TypeError("Only Products can be added.")

    def remove_product(self, product):
        if product in self.products:
            self.products.remove(product)

    def get_total_quantity(self):
        return sum(product.get_quantity() for product in self.products)

    def get_all_products(self):
        return [product for product in self.products if product.is_active()]

    def order(self, shopping_list):
        total_price = 0.0
        for product, quantity in shopping_list:
            total_price += product.buy(quantity)
        return total_price