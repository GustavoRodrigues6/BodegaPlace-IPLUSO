connection = sqlite3.connect('wines.db')
cursor = connection.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS wines(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    brand TEXT,
    year TEXT,
    price TEXT,
    region TEXT,
    description TEXT,
    nutrition DOUBLE,
    supplier INTEGER,
    stock INTEGER,
    FOREIGN KEY (supplier) REFERENCES users(id)
    )
''')
connection.commit()