class ProductError(Exception):
    """Custom exception for product-related errors."""
    pass

class OutOfStockError(Exception):
    """Raised when a product is out of stock."""
    pass

class Product:
    def __init__(self, name: str, price: float, quantity: int):
        """Initializes a product with validation."""
        if not name or not isinstance(name, str):
            raise ProductError("Product name must be a non-empty string.")
        if not isinstance(price, (int, float)) or price <= 0:
            raise ProductError("Price must be a positive number.")
        if not isinstance(quantity, int) or quantity < 0:
            raise ProductError("Quantity must be a non-negative integer.")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def is_active(self) -> bool:
        """Returns whether the product is active."""
        return self.active

    def activate(self):
        """Activates the product."""
        self.active = True

    def deactivate(self):
        """Deactivates the product."""
        self.active = False

    def set_quantity(self, new_quantity: int):
        """Updates the product quantity."""
        if not isinstance(new_quantity, int) or new_quantity < 0:
            raise ProductError("Quantity must be a non-negative integer.")
        self.quantity = new_quantity

    def get_quantity(self) -> int:
        """Returns the current quantity."""
        return self.quantity

    def buy(self, amount: int) -> float:
        """Processes a purchase and deactivates if stock reaches zero."""
        if not self.active:
            raise ProductError("Cannot buy inactive product.")
        if not isinstance(amount, int) or amount <= 0:
            raise ProductError("Purchase amount must be a positive integer.")
        if amount > self.quantity:
            raise OutOfStockError(f"Only {self.quantity} units available.")

        self.quantity -= amount
        total_price = self.price * amount

        if self.quantity == 0:
            self.deactivate()

        return total_price

    def show(self):
        """Displays product details."""
        status = "Active" if self.active else "Inactive"
        print(f"{self.name} - ${self.price} ({self.quantity} in stock) [{status}]")


