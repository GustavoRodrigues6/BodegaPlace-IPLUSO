import sqlite3

# Função para criar e popular a tabela de vendas mensais
def criar_tabela_vendas():
    conn = sqlite3.connect('vendas.db')
    cursor = conn.cursor()
    
    # Criar a tabela de vendas mensais
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS vendas_mensais (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        mes TEXT,
        ano INTEGER,
        valor_venda REAL
    )
    ''')
    
    # Inserir alguns dados de exemplo
    cursor.executemany('''
    INSERT INTO vendas_mensais (mes, ano, valor_venda)
    VALUES (?, ?, ?)
    ''', [
        ('Janeiro', 2023, 15000.75),
        ('Fevereiro', 2023, 12500.50),
        ('Março', 2023, 17500.00),
        ('Abril', 2023, 16000.20)
    ])
    
    conn.commit()
    conn.close()

# Função para visualizar a tabela de vendas mensais
def visualizar_tabela_vendas():
    conn = sqlite3.connect('vendas.db')
    df = pd.read_sql_query('SELECT * FROM vendas_mensais', conn)
    conn.close()
    print(df)
    return df

# Função para exportar a tabela de vendas para CSV
def exportar_tabela_vendas(df):
    df.to_csv('vendas_mensais.csv', index=False)
    print("A tabela de vendas mensais foi exportada para 'vendas_mensais.csv'")

# Criar e popular a tabela de vendas
criar_tabela_vendas()

# Visualizar a tabela de vendas
df = visualizar_tabela_vendas()

# Exportar a tabela de vendas para CSV
exportar_tabela_vendas(df)
