# BodegaPlace 🍷

BodegaPlace é a sua plataforma completa para gerenciar sua coleção de vinhos. Desde a adição de novas garrafas até a análise dos seus hábitos de consumo, oferecemos uma experiência personalizada e intuitiva para os amantes de vinho.

## 📋 Funcionalidades

### 📦 Gestão de Estoque:
**- Inserção de novos vinhos:** Permite adicionar novos produtos ao catálogo, com informações como marca, preço, região, ano e descrição.

**- Edição de vinhos:** Possibilita a atualização de informações de vinhos já cadastrados.

**- Exclusão de vinhos:** Permite remover vinhos descontinuados do catálogo.
### 📈 Análise de Vendas:
**- Tabela de vendas mensais:** Apresenta uma visão geral das vendas por mês.

**- Exportação de dados:** Permite exportar os dados de vendas em formato CSV para análise mais detalhada.
### ⚙️ Funcionalidades para Usuários:
**- Registo e autenticação:** Criação de contas de usuário com informações pessoais e login seguro.

**- Exploração do catálogo:** Permite aos usuários navegar e pesquisar por vinhos disponíveis.

**- Carrinho de compras:** Possibilita aos usuários adicionar produtos ao carrinho e realizar compras (implementação futura).

**- Gerenciamento de conta:** Permite aos usuários atualizar suas informações pessoais e excluir suas contas.

## 🛠️ Tecnologias Utilizadas

- Python 🐍
- SQLite3 (banco de dados local)
- CustomTkinter (interface gráfica)

## ▶️ Como Executar o Projeto

### Pré-requisitos

Certifique-se de ter o **Python 3.10** ou superior instalado e as dependências necessárias.

### 1. Clone o repositório:

```bash
git clone https://github.com/GustavoRodrigues6/bodegaplace-ipluso.git
cd bodegaplace-ipluso
```

### 2. Crie um ambiente virtual:

```bash
python -m venv venv
source venv/bin/activate  # No Windows, use: venv\Scripts\activate
```

### 3. Instale as dependências:

```bash
pip install -r requirements.txt
```

### 4. Execute a aplicação:

```bash
python src/app.py
```

## 🗂️ Estrutura do Projeto

```plaintext
📁 bodegaplace
├── 📂 assets                 # Recursos visuais
├── 📂 db
│   ├── db.py                 # Funções para manipulação do banco de dados
├── 📂 src
│   ├── app.py                # Arquivo principal da aplicação
│   ├── interface.py          # Funções da interface gráfica
│   ├── users.py              # Gerenciamento de usuários
│   └── utils.py              # Funções auxiliares
├── README.md                 # Documentação do projeto
```


