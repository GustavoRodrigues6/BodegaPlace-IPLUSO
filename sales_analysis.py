import sqlite3
import pandas as pd

# Function to create and populate the monthly sales table
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

# Function to view the monthly sales table
def view_sales_table():
    conn = sqlite3.connect('sales.db')
    df = pd.read_sql_query('SELECT * FROM monthly_sales', conn)
    conn.close()
    print(df)
    return df

# Function to export the sales table to CSV
def export_sales_table(df):
    df.to_csv('monthly_sales.csv', index=False)
    print("The monthly sales table has been exported to 'monthly_sales.csv'")

# Create and populate the sales table
create_sales_table()

# View the sales table
df = view_sales_table()

# Export the sales table to CSV
export_sales_table(df)
