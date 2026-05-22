y# item.py
# Contains the StationeryItem class to calculate total price

class StationeryItem:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price
        self.total_price = self.calculate_total()

    def calculate_total(self):
        # Returns total price based on quantity and price
        return self.quantity * self.price