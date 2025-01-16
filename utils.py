import sqlite3

def is_admin(uid):
    """
    Check if user is admin
    :param uid: User ID
    :return: boolean true if user is admin, false if not
    """
    connection = sqlite3.connect('users.db')
    cursor = connection.cursor()
    
    cursor.execute("SELECT is_admin FROM users WHERE id = ?", (uid,))
    result = cursor.fetchone()
    
    connection.close()
    
    if result:
        return result[0] == 1
    return False


def get_wine_supplier(uid):
    """
    Get supplier ID of a wine
    :param uid: User ID
    :return: Supplier ID
    """
    connection = sqlite3.connect('users.db')
    cursor = connection.cursor()

    cursor.execute("SELECT supplier FROM users WHERE id = ?", (uid,))
    result = cursor.fetchone()

    connection.close()

    if result:
        return result[0]
    return None


def get_wine_stock(wid):
    """
    Get stock of a wine
    :param wid: Wine ID
    :return: Stock
    """
    connection = sqlite3.connect('wines.db')
    cursor = connection.cursor()

    cursor.execute("SELECT stock FROM wines WHERE id = ?", (wid,))
    result = cursor.fetchone()

    connection.close()

    if result:
        return result[0]
    return None