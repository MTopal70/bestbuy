class Product:
    def __init__(self, name, price, quantity):
        if not name or price < 0 or quantity < 0:
            raise ValueError("Ungültige Produktdaten: Name darf nicht leer sein, Preis und Menge müssen ≥ 0 sein.")
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self):
        return self.quantity

    def set_quantity(self, quantity):
        if quantity < 0:
            raise ValueError("Menge darf nicht negativ sein.")
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
            raise Exception("Produkt ist nicht aktiv.")
        if quantity <= 0:
            raise ValueError("Kaufmenge muss positiv sein.")
        if quantity > self.quantity:
            raise Exception("Nicht genügend Lagerbestand.")
        self.quantity -= quantity
        if self.quantity == 0:
            self.deactivate()
        return self.price * quantityx