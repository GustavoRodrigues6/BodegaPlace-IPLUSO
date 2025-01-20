import sqlite3

def create_cart_db():
    connection = sqlite3.connect('cart.db')
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cart(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        wine_id INTEGER,
        FOREIGN KEY(user_id) REFERENCES users(id)
        )
    ''')

if __name__ == "__main__":
    create_cart_db()
