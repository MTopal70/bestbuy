from abc import ABC, abstractmethod


class Promotion(ABC):
    """Abstract base class for promotions."""

    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def apply_promotion(self, product, quantity) -> float:
        """Returns the discounted price."""
        pass


class PercentDiscount(Promotion):
    """Percentage discount promotion."""

    def __init__(self, name: str, percent: float):
        super().__init__(name)
        self.percent = percent

    def apply_promotion(self, product, quantity) -> float:
        total = product.price * quantity
        discount = total * (self.percent / 100)
        return total - discount


class SecondHalfPrice(Promotion):
    """Second item is half price."""

    def apply_promotion(self, product, quantity) -> float:
        full_price_items = quantity // 2 + quantity % 2
        half_price_items = quantity // 2

        return full_price_items * product.price + half_price_items * (product.price / 2)


class ThirdOneFree(Promotion):
    """Buy 2, get 1 free."""

    def apply_promotion(self, product, quantity) -> float:
        free_items = quantity // 3
        paid_items = quantity - free_items
        return paid_items * product.price