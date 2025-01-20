import sqlite3
from users import User 

class User:
    def __init__(self, id, username, email, password, address1, address2, nif, is_admin):
        self.id = id
        self.username = username
        self.email = email
        self.password = password
        self.address1 = address1
        self.address2 = address2
        self.nif = nif
        self.is_admin = is_admin


def user_register(username, email, password, address1, address2):
    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()
    cursor.execute('''
        INSERT INTO users (username, email, password, address1, address2)
        VALUES (?, ?, ?, ?, ?)
    ''', (username, email, password, address1, address2))
    connection.commit()
    connection.close()

def update_user(user_id, username, email, address1, address2):
    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()
    cursor.execute('''
        UPDATE users
        SET username = ?, email = ?, address1 = ?, address2 = ?
        WHERE id = ?
    ''', (username, email, address1, address2, user_id))
    connection.commit()
    connection.close()

def delete_user(user_id):
    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()
    cursor.execute('DELETE FROM users WHERE id = ?', (user_id,))
    connection.commit()
    connection.close()

def get_user(user_id):
    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM users WHERE id = ?', (user_id))
    user = cursor.fetchone()
    connection.close()
    return User(*user) if user else None