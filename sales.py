from db_wines import WINES

class Wine:
    def __init__(self, name, brand, year, price, stock, supplier):
        self.name = name
        self.brand = brand
        self.year = year
        self.price = price
        self.stock = stock
        self.supplier = supplier

    def sell(self, quantity):
        if quantity <= self.stock:
            self.stock -= quantity
            total_price = quantity * self.price
            print(f'Sold {quantity} bottles of {self.brand} {self.name} ({self.year}) for ${total_price:.2f}')
        else:
            print(f'Not enough stock to sell {quantity} bottles of {self.brand} {self.name} ({self.year})')

    def restock(self, quantity):
        self.stock += quantity
        print(f'Restocked {quantity} bottles of {self.brand} {self.name} ({self.year}). New stock: {self.stock}')

def initialize_wines(wine_data):
    wines = []
    for wine in wine_data:
        wine_obj = Wine(
            name=wine["Brand"],
            brand=wine["Brand"],
            year=wine["Year"],
            price=wine["Price"],
            stock=wine["Stock"],
            supplier=wine["Supplier"]
        )
        wines.append(wine_obj)
    return wines

