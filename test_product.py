import pytest
from products import Product, ProductError, OutOfStockError

def test_create_normal_product():
    """Creates a normal product."""
    p = Product("MacBook Air M2", price=1450, quantity=100)
    assert p.name == "MacBook Air M2"
    assert p.price == 1450
    assert p.quantity == 100
    assert p.is_active() is True

def test_create_invalid_product():
    """Invalid product details should raise an exception."""
    # Empty name

    with pytest.raises(ProductError):
        Product("", price=1450, quantity=100)

    # Negative Price

    with pytest.raises(ProductError):
        Product("MacBook Air M2", price=-10, quantity=100)

    # Negative quantity

    with pytest.raises(ProductError):
        Product("MacBook Air M2", price=1450, quantity=-5)


def test_product_becomes_inactive_at_zero_quantity():
    """Product should deactivate when quantity reaches zero."""
    p = Product("Pixel 7", price=500, quantity=1)
    p.buy(1)
    assert p.get_quantity() == 0
    assert p.is_active() is False


def test_purchase_modifies_quantity_and_returns_price():
    """Buying a product should reduce quantity and return correct total price."""
    p = Product("Bose Earbuds", price=250, quantity=10)
    total = p.buy(2)
    assert total == 500
    assert p.get_quantity() == 8


def test_buying_more_than_available_raises_exception():
    """Buying more than available should raise OutOfStockError."""
    p = Product("Google Pixel 7", price=500, quantity=5)
    with pytest.raises(OutOfStockError):
        p.buy(10)

