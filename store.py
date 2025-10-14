from products import Product, OutOfStockError

class Store:
    """
    Manages a list of Product instances and allows adding/removing products.
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
        else:
            raise ValueError("Product not found in store.")

    def get_total_quantity(self):
        return sum(product.get_quantity() for product in self.products)

    def get_all_products(self):
        return [product for product in self.products if product.is_active()]

    def order(self, shopping_list):
        for product, quantity in shopping_list:
            if quantity > product.get_quantity():
                raise OutOfStockError(f"{product.name} has only {product.get_quantity()} units left.")
        total_price = sum(product.buy(quantity) for product, quantity in shopping_list)
        return total_price


