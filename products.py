class OutOfStockError(Exception):
    """Custom exception raised when requested quantity exceeds available stock."""
    pass


class Product:
    """
    Represents a product in the BestBuy store.

    Attributes:
        name (str): Name of the product.
        price (float): Price per unit.
        quantity (int): Available stock.
        active (bool): Whether the product is active and available for sale.
    """

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def buy(self, amount):
        """
        Attempts to purchase a given quantity of the product.

        Args:
            amount (int): Quantity to purchase.

        Returns:
            float: Total price for the purchase.

        Raises:
            OutOfStockError: If requested amount exceeds available quantity.
            ValueError: If amount is not positive.
        """
        if amount <= 0:
            raise ValueError("Purchase quantity must be positive.")
        if amount > self.quantity:
            raise OutOfStockError(
                f"Not enough stock for '{self.name}'. Requested: {amount}, Available: {self.quantity}"
            )
        self.quantity -= amount
        return self.price * amount

    def get_quantity(self):
        """Returns the current quantity of the product."""
        return self.quantity

    def is_active(self):
        """Returns True if the product is active and has stock."""
        return self.active and self.quantity > 0

    def show(self):
        """Displays product details."""
        print(f"{self.name}, Price: ${self.price}, Quantity: {self.quantity}")