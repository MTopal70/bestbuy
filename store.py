from products import Product

class Store:
    """
    This module defines the Store class.
    It manages a list of Product instances and allows adding/removing products.
    It can calculate total quantity and process multi-product orders.
    """

    def __init__(self, products=None):
      """Initializes the store with a list of products."""
      if products is None:
          products = []
      self.products = products

    def add_product(self, product):
      """Adds a product to the store."""
      if isinstance(product, Product):
          self.products.append(product)
      else:
          raise TypeError("Only Products can be added.")

    def remove_product(self, product):
      """Removes a product from the store."""
      if product in self.products:
          self.products.remove(product)

    def get_total_quantity(self):
      """Returns the total quantity of all products in the store."""
      return sum(product.get_quantity() for product in self.products)

    def get_all_products(self):
      """Returns a list of all active products in the store."""
      return [product for product in self.products if product.is_active()]

    def order(self, shopping_list):
      """
        Processes a list of product orders.
        Each item in the list is a tuple of (Product, quantity).
        Returns the total price of the order.
      """
      total_price = 0.0
      for product, quantity in shopping_list:
          total_price += product.buy(quantity)
      return total_price
