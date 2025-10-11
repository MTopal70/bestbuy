class Product:
    """
    This module defines the Product class.
    It represents a single product in the store, with name, price, quantity, and active status.
    It includes methods to buy products, update quantity, and show product details.
    """

    def __init__(self, name, price, quantity):
        if not name or price < 0 or quantity < 0:
            raise ValueError("Invalid product data: Name can't be empty, price and quantity have to be ≥ 0 ")
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self):
        return self.quantity

    def set_quantity(self, quantity):
        if quantity < 0:
            raise ValueError("Quantity must be greater than zero.")
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def is_active(self):
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self):
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")

    def buy(self, quantity):
        if not self.active:
            raise Exception("Product is not active.")
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")
        if quantity > self.quantity:
            raise Exception("Not enough product available.")
        self.quantity -= quantity
        if self.quantity == 0:
            self.deactivate()
        return self.price * quantity