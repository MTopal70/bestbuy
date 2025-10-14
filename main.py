"""
Main user interface module for BestBuy store.
Sets up the initial inventory and provides a menu for interacting with the store.
Users can list products, check total quantity, place orders, or exit the program.
"""

from products import Product, OutOfStockError
from store import Store

# Initial inventory
product_list = [
    Product("MacBook Air M2", price=1450, quantity=100),
    Product("Bose QuietComfort Earbuds", price=250, quantity=500),
    Product("Google Pixel 7", price=500, quantity=250),
]

best_buy = Store(product_list)

def list_products(store):
    """Displays all active products."""
    print("\nAvailable Products:")
    for product in store.get_all_products():
        product.show()

def show_total(store):
    """Displays total quantity in store."""
    total = store.get_total_quantity()
    print(f"\nTotal quantity in store: {total}")

def make_order(store):
    """Handles user order input."""
    print("\nEnter your order:")
    shopping_list = []

    while True:
        active_products = store.get_all_products()  # Refresh product list each time
        print("\nAvailable Products:")
        for i, product in enumerate(active_products):
            print(f"{i + 1}. {product.name} (Available: {product.get_quantity()})")

        selection = input("Select product number (or 'done' to finish): ")
        if selection.lower() == "done":
            break
        try:
            index = int(selection) - 1
            if index < 0 or index >= len(active_products):
                print("Invalid product number.")
                continue

            product = active_products[index]
            quantity = int(input(f"Enter quantity for {product.name}: "))
            if quantity <= 0:
                print("Quantity must be greater than zero.")
                continue
            # Calculate already ordered amount of the product
            already_ordered = sum(qty for p, qty in shopping_list if p == product)
            available = product.get_quantity() - already_ordered

            if quantity > available:
                print(
                    f"Only {available} units available (after {already_ordered} already in cart). Cannot add {quantity}.")
                continue

            shopping_list.append((product, quantity))
            print(f"Added {quantity} x {product.name} to your cart.")
        except ValueError:
            print("Please enter a valid number.")
            continue

    if not shopping_list:
        print("\n🛒 No items in cart. Order cancelled.")
        return

    print("\n🛒 Your shopping cart:")
    for product, qty in shopping_list:
        print(f"- {qty} x {product.name}")

    try:
        total_price = store.order(shopping_list)
        print(f"\nOrder successful! Total price: {total_price} dollars.")
    except OutOfStockError as stock_error:
        print(f"Stock issue: {stock_error}")
    except ValueError as val_error:
        print(f"Invalid quantity: {val_error}")
    except Exception as error:
        print(f"Unexpected error: {error}")

def start(store):
    """Starts the interactive CLI menu."""
    while True:
        print("\n--- BestBuy Store Menu ---")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            list_products(store)
        elif choice == "2":
            show_total(store)
        elif choice == "3":
            make_order(store)
        elif choice == "4":
            print("Thank you for visiting BestBuy. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a number between 1 and 4.")

if __name__ == "__main__":
    start(best_buy)



