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

# Example usage
if __name__ == "__main__":
    wine1 = Wine("Cabernet Sauvignon", "Brand A", 2015, 20.0, 50, "Supplier X")
    wine2 = Wine("Merlot", "Brand B", 2018, 15.0, 30, "Supplier Y")

    wine1.sell(10)
    wine2.sell(5)
    wine1.restock(20)
    wine2.sell(50)