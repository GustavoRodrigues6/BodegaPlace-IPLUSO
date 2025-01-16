import sqlite3
from users import User  

def user_register(username, email, password, address1, address2=None):
    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()
    cursor.execute('''
        INSERT INTO users (username, email, password, address1, address2)
        VALUES (?, ?, ?, ?, ?)
    ''', (username, email, password, address1, address2))
    connection.commit()
    connection.close()

def update_user(user_id, username, email, address1, address2=None):
    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()
    cursor.execute('''
        UPDATE users
        SET username = ?, email = ?, address1 = ?, address2 = ?
        WHERE id = ?
    ''', (username, email, address1, address2, user_id))
    connection.commit()
    connection.close()

def excluir_usuario(user_id):
    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()
    cursor.execute('DELETE FROM users WHERE id = ?', (user_id,))
    connection.commit()
    connection.close()

