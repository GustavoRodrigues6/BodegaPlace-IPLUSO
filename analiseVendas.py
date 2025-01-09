import pandas as pd
import matplotlib.pyplot as plt

# Dados fictícios de vendas mensais
dados_vendas = {
    'Mês': ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'],
    'Vendas': [1500, 2300, 1800, 2200, 2500, 2700, 3000, 3200, 3100, 2900, 3300, 3600]
}

# Criação do DataFrame
df_vendas = pd.DataFrame(dados_vendas)

# Visualização da tabela de vendas mensais
print("Tabela de Vendas Mensais:")
print(df_vendas)

# Exportação da tabela de vendas em formato CSV
df_vendas.to_csv('tabela_vendas_mensais.csv', index=False)
print("Tabela de vendas exportada para 'tabela_vendas_mensais.csv'.")

# Plotando o gráfico de vendas mensais
plt.figure(figsize=(10, 5))
plt.plot(df_vendas['Mês'], df_vendas['Vendas'], marker='o')
plt.title('Vendas Mensais')
plt.xlabel('Mês')
plt.ylabel('Vendas')
plt.grid(True)
plt.show()