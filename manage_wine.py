import sqlite3
from wines import Wine

def insert_wines(brand, year, price, region, description, nutrition, supplier, stock):
    connection = sqlite3.connect('wines.db')
    cursor = connection.cursor()
    cursor.execute('''
        INSERT INTO wines(brand, year, price, region, description, nutrition, supplier, stock)
        VALUES(?, ?, ?, ?, ?, ?, ?, ?)
    ''', (brand, year, price, region, description, nutrition, supplier, stock))
    connection.commit()
    connection.close()

def get_wines():
    connection = sqlite3.connect('wines.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM wines')
    wines = cursor.fetchall()
    connection.close()
    return [Wine(*wine) for wine in wines]

def get_wine_by_id(wine_id):
    connection = sqlite3.connect('wines.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM wines WHERE id = ?', (wine_id,))
    wine = cursor.fetchone()
    connection.close()
    return Wine(*wine) if wine else None

def update_wine(wine_id, brand, year, price, region, description, nutrition, supplier, stock):
    connection = sqlite3.connect('wines.db')
    cursor = connection.cursor()
    cursor.execute('''
        UPDATE wines
        SET brand = ?, year = ?, price = ?, region = ?, description = ?, nutrition = ?, supplier = ?, stock = ?
        WHERE id = ?
    ''', (brand, year, price, region, description, nutrition, supplier, stock, wine_id))
    connection.commit()
    connection.close()

def delete_wine(wine_id):
    connection = sqlite3.connect('wines.db')
    cursor = connection.cursor()
    cursor.execute('DELETE FROM wines WHERE id = ?', (wine_id,))
    connection.commit()
    connection.close()

#Caso quisermos fazer uma filtros de busca
def get_wines_by_supplier(supplier_id):
    connection = sqlite3.connect('wines.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM wines WHERE supplier = ?', (supplier_id,))
    wines = cursor.fetchall()
    connection.close()
    return [Wine(*wine) for wine in wines]

def get_wines_by_region(region):
    connection = sqlite3.connect('wines.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM wines WHERE region = ?', (region,))
    wines = cursor.fetchall()
    connection.close()
    return [Wine(*wine) for wine in wines]

def get_wines_by_price(price):
    connection = sqlite3.connect('wines.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM wines WHERE price = ?', (price,))
    wines = cursor.fetchall()
    connection.close()
    return [Wine(*wine) for wine in wines]

def get_wines_by_year(year):
    connection = sqlite3.connect('wines.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM wines WHERE year = ?', (year,))
    wines = cursor.fetchall()
    connection.close()
    return [Wine(*wine) for wine in wines]
