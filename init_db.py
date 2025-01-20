import sqlite3

def create_users_db():
    connection = sqlite3.connect('users.db')
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        email TEXT,
        password TEXT,
        address1 TEXT,
        address2 TEXT,
        nif INTEGER,
        is_admin INTEGER,
        CONSTRAINT email UNIQUE(email)
        )
    ''')

    users = [
        ("admin", "admin@example.com", "adminpass", "Address 1", "Address 2", 123456789, 1),
        ("user1", "user1@example.com", "user1pass", "Address 1", "Address 2", 987654321, 0),
        ("user2", "user2@example.com", "user2pass", "Address 1", "Address 2", 192837465, 0)
    ]

    cursor.executemany('''
        INSERT INTO users (username, email, password, address1, address2, nif, is_admin)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', users)

    connection.commit()
    connection.close()

def create_wines_db():
    connection = sqlite3.connect('wines.db')
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS wines(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        brand TEXT,
        year INTEGER,
        price REAL,
        region TEXT,
        description TEXT,
        nutrition REAL,
        supplier INTEGER,
        stock INTEGER,
        FOREIGN KEY (supplier) REFERENCES users(id)
        )
    ''')

    wines = [
        ("Vinho do Porto", 2015, 25.0, "Douro", "Um vinho fortificado, doce e encorporado", 20, 1, 23),
        ("Château Margaux", 2018, 450.0, "Bordeaux", "Elegante e encorpado, com notas de frutas vermelhas", 14, 2, 124),
        ("Penfolds Grange", 2020, 700.0, "Barossa Valley", "Frutas escuras e taninos sedosos", 15, 3, 85)
    ]

    cursor.executemany('''
        INSERT INTO wines (brand, year, price, region, description, nutrition, supplier, stock)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', wines)

    connection.commit()
    connection.close()

def create_sales_table():
    conn = sqlite3.connect('sales.db')
    cursor = conn.cursor()
    
    # Create the monthly sales table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS monthly_sales (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        month TEXT,
        year INTEGER,
        sales_value REAL
    )
    ''')
    
    # Insert some sample data
    cursor.executemany('''
    INSERT INTO monthly_sales (month, year, sales_value)
    VALUES (?, ?, ?)
    ''', [
        ('January', 2023, 15000.75),
        ('February', 2023, 12500.50),
        ('March', 2023, 17500.00),
        ('April', 2023, 16000.20)
    ])
    
    conn.commit()
    conn.close()


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
    connection.commit()
    connection.close()

if __name__ == "__main__":
    create_users_db()
    create_wines_db()
    create_sales_table()
    create_cart_db()
    print("Databases created and populated with sample data.")