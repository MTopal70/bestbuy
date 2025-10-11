"""
Main user interface module for BestBuy store.
Sets up the initial inventory and provides a menu for interacting with the store.
Users can list products, check total quantity, place orders, or exit the program.
"""

from products import Product
from store import Store

# Setup initial stock of inventory
product_list = [
    Product("MacBook Air M2", price=1450, quantity=100),
    Product("Bose QuietComfort Earbuds", price=250, quantity=500),
    Product("Google Pixel 7", price=500, quantity=250),
]

best_buy = Store(product_list)


def list_products(store):
    """Displays all active products in the store."""
    print("\nAvailable Products:")
    for product in store.get_all_products():
        product.show()


def show_total(store):
    """Displays total quantity of all products in the store."""
    total = store.get_total_quantity()
    print(f"\nTotal quantity in store: {total}")


def make_order(store):
    """Handles the order process from user input."""
    print("\nEnter your order:")
    active_products = store.get_all_products()
    shopping_list = []

    for i, product in enumerate(active_products):
        print(f"{i + 1}. {product.name} (Available: {product.get_quantity()})")

    while True:
        selection = input("Select product number (or 'done' to finish): ")
        if selection.lower() == "done":
            break
        try:
            index = int(selection) - 1
            if index < 0 or index >= len(active_products):
                print("Invalid product number.")
                continue
            quantity = int(input(f"Enter quantity for {active_products[index].name}: "))
            shopping_list.append((active_products[index], quantity))
        except ValueError as error:
            print(f"Invalid input: {error}")

    try:
        total_price = store.order(shopping_list)
        print(f"\nOrder successful! Total price: {total_price} dollars.")
    except ValueError as val_error:
        print(f"Invalid quantity: {val_error}")
    except RuntimeError as runtime_error:
        print(f"Order processing error: {runtime_error}")

def start(store):
    """Starts the interactive menu for the store."""
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
