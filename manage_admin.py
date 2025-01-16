import sqlite3

def update_wine(wine_id, brand, year, price, region, description, nutrition, supplier, stock):
    """
    Update wine information
    :param wine_id: Wine ID
    :param brand: Wine brand
    :param year: Wine year
    :param price: Wine price
    :param region: Wine region
    :param description: Wine description
    :param nutrition: Wine nutrition
    :param supplier: Supplier ID
    :param stock: Wine stock
    """
    connection = sqlite3.connect("wines.db")
    cursor = connection.cursor()
    cursor.execute('''
        UPDATE wines
        SET brand = ?, year = ?, price = ?, region = ?, description = ?, nutrition = ?, supplier = ?, stock = ?
        WHERE id = ?
    ''', (brand, year, price, region, description, nutrition, supplier, stock, wine_id))
    connection.commit()
    connection.close()

def delete_wine(wine_id):
    """
    Delete wine
    :param wine_id: Wine ID
    """
    connection = sqlite3.connect("wines.db")
    cursor = connection.cursor()
    cursor.execute('DELETE FROM wines WHERE id = ?', (wine_id,))
    connection.commit()
    connection.close()

def search_user_by_nif(user_nif):
    """
    Search user by NIF
    :param user_nif: User NIF
    :return: User ID
    """
    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()
    cursor.execute("SELECT id FROM users WHERE nif = ?", (user_nif,))
    result = cursor.fetchone()
    connection.close()
    if result:
        return result[0]
    return None
