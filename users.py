connection = sqlite3.connect('users.db')
cursor = connection.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT,
    password TEXT,
    address_1 TEXT,
    address_2 TEXT,
    nif INTEGER,
    is_admin INTEGER,
    CONSTRAINT email UNIQUE(email)
    )
''')
connection.commit()