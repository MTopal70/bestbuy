class OutOfStockError(Exception):
    """Custom exception raised when requested quantity exceeds available stock."""
    pass


class Product:
    """
    Represents a product in the BestBuy store.
    """

    def __init__(self, name, price, quantity):
        if not name or not name.strip():
            raise ValueError("Product name cannot be empty.")
        if price < 0:
            raise ValueError("Price cannot be negative.")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def buy(self, amount):
        if amount <= 0:
            raise ValueError("Purchase quantity must be positive.")
        if amount > self.quantity:
            raise OutOfStockError(
                f"Not enough stock for '{self.name}'. Requested: {amount}, Available: {self.quantity}"
            )
        self.quantity -= amount
        if self.quantity == 0:
            self.deactivate()
        return self.price * amount

    def get_quantity(self):
        return self.quantity

    def is_active(self):
        return self.active

    def set_quantity(self, quantity):
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self):
        print(f"{self.name}, Price: ${self.price}, Quantity: {self.quantity}")

