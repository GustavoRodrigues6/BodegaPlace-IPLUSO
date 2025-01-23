import sqlite3
import customtkinter as ctk
from tkinter import messagebox
from manage_wine import get_wines, insert_wine

def clear_screen(frame: ctk.CTk):
    for widget in frame.winfo_children():
        widget.destroy()

def set_widget_style(widget, font: tuple = ("Arial", 12), padding: int = 5):
    widget.configure(font=font, padx=padding, pady=padding)

def show_info_message(title: str, message: str):
    messagebox.showinfo(title, message)

def show_error_message(title: str, message: str):
    messagebox.showerror(title, message)

def show_confirmation_message(title: str, message: str) -> bool:
    return messagebox.askyesno(title, message)

def create_label(parent: ctk.CTk, text: str, font: tuple = ("Arial", 12), anchor: str = "w") -> ctk.CTkLabel:
    label = ctk.CTkLabel(parent, text=text, font=font, anchor=anchor)
    return label

def create_button(parent: ctk.CTk, text: str, command, font: tuple = ("Arial", 12)) -> ctk.CTkButton:
    button = ctk.CTkButton(parent, text=text, command=command, font=font)
    return button

def create_entry(parent: ctk.CTk, placeholder: str = "", font: tuple = ("Arial", 12), show: str = "") -> ctk.CTkEntry:
    entry = ctk.CTkEntry(parent, placeholder_text=placeholder, font=font, show=show)
    return entry

def center_window(window: ctk.CTk, width: int, height: int):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    window.geometry(f"{width}x{height}+{x}+{y}")

def table_wines_admin(parent: ctk.CTk):
    frame_cabecalho = ctk.CTkFrame(parent, width=500, height=30)
    frame_cabecalho.grid(row=0, column=0, padx=10, pady=5, sticky="w")
    ctk.CTkLabel(frame_cabecalho, text="Marca", font=("Arial", 12, "bold"), anchor="w", width=150).grid(row=0, column=1, padx=(10, 5), pady=2)
    ctk.CTkLabel(frame_cabecalho, text="Ano", font=("Arial", 12, "bold"), anchor="center", width=50).grid(row=0, column=2, padx=5, pady=2)
    ctk.CTkLabel(frame_cabecalho, text="Preço", font=("Arial", 12, "bold"), anchor="center", width=50).grid(row=0, column=3, padx=5, pady=2)
    ctk.CTkLabel(frame_cabecalho, text="Região", font=("Arial", 12, "bold"), anchor="w", width=120).grid(row=0, column=4, padx=5, pady=2)

    frame_tabela = ctk.CTkScrollableFrame(parent, width=450, height=250)
    frame_tabela.grid(row=1, column=0, padx=10, pady=5, sticky="w")

    wines = get_wines()
    if wines:
        for i, wine in enumerate(wines):
            ctk.CTkLabel(frame_tabela, text=f"{wine[1]}", anchor="w", width=150).grid(row=i + 1, column=1, padx=5, pady=2)
            ctk.CTkLabel(frame_tabela, text=f"{wine[2]}", anchor="center", width=50).grid(row=i + 1, column=2, padx=5, pady=2)
            ctk.CTkLabel(frame_tabela, text=f"{wine[3]}", anchor="center", width=50).grid(row=i + 1, column=3, padx=5, pady=2)
            ctk.CTkLabel(frame_tabela, text=f"{wine[4]}", anchor="w", width=120).grid(row=i + 1, column=4, padx=5, pady=2)
    else:
        ctk.CTkLabel(frame_tabela, text="Nenhum vinho cadastrado!", font=("Arial", 12), anchor="center").grid(row=1, column=0, columnspan=5, pady=10)

def table_wines_user(parent: ctk.CTk, search_term: str = ""):
    frame_cabecalho = ctk.CTkFrame(parent, width=500, height=30)
    frame_cabecalho.grid(row=1, column=0, padx=10, pady=5, sticky="w")
    ctk.CTkLabel(frame_cabecalho, text="Marca", font=("Arial", 12, "bold"), anchor="w", width=150).grid(row=0, column=1, padx=(10, 5), pady=2)
    ctk.CTkLabel(frame_cabecalho, text="Ano", font=("Arial", 12, "bold"), anchor="center", width=50).grid(row=0, column=2, padx=5, pady=2)
    ctk.CTkLabel(frame_cabecalho, text="Preço", font=("Arial", 12, "bold"), anchor="center", width=50).grid(row=0, column=3, padx=5, pady=2)
    ctk.CTkLabel(frame_cabecalho, text="Região", font=("Arial", 12, "bold"), anchor="w", width=120).grid(row=0, column=4, padx=5, pady=2)

    frame_tabela = ctk.CTkScrollableFrame(parent, width=450, height=250)
    frame_tabela.grid(row=2, column=0, padx=10, pady=5, sticky="w")

    wines = get_wines()
    if wines:
        filtered_wines = [wine for wine in wines if search_term.lower() in wine[1].lower()]
        for i, wine in enumerate(filtered_wines):
            ctk.CTkLabel(frame_tabela, text=f"{wine[1]}", anchor="w", width=150).grid(row=i + 1, column=1, padx=5, pady=2)
            ctk.CTkLabel(frame_tabela, text=f"{wine[2]}", anchor="center", width=50).grid(row=i + 1, column=2, padx=5, pady=2)
            ctk.CTkLabel(frame_tabela, text=f"{wine[3]}", anchor="center", width=50).grid(row=i + 1, column=3, padx=5, pady=2)
            ctk.CTkLabel(frame_tabela, text=f"{wine[4]}", anchor="w", width=120).grid(row=i + 1, column=4, padx=5, pady=2)
    else:
        ctk.CTkLabel(frame_tabela, text="Nenhum vinho cadastrado!", font=("Arial", 12), anchor="center").grid(row=1, column=0, columnspan=5, pady=10)

def buy_wine(wine_name: str, user_id: int):
    connection = sqlite3.connect('cart.db')
    cursor = connection.cursor()
    wines = get_wines()
    selected_wine = next((wine for wine in wines if wine_name.lower() in wine[1].lower()), None)
    
    if selected_wine:
        cursor.execute('INSERT INTO cart (user_id, wine_id) VALUES (?, ?)', (user_id, selected_wine[0]))
        connection.commit()
        show_info_message("Compra", f"Vinho {selected_wine[1]} adicionado ao carrinho!")
    else:
        show_error_message("Erro", "Vinho não encontrado!")
    connection.close()

def show_cart(user_id: int):
    connection = sqlite3.connect('cart.db')
    cursor = connection.cursor()
    cursor.execute('''
        SELECT wines.id, wines.brand, wines.year, wines.price, wines.region
        FROM cart
        JOIN wines ON cart.wine_id = wines.id
        WHERE cart.user_id = ?
    ''', (user_id,))
    cart_items = cursor.fetchall()
    connection.close()

    cart_window = ctk.CTk()
    cart_window.title("Carrinho de Compras")
    center_window(cart_window, 600, 400)

    cart_frame = ctk.CTkFrame(cart_window)
    cart_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    create_label(cart_frame, text="Carrinho de Compras", font=("Arial", 16), anchor="w").grid(row=0, column=0, padx=10, pady=5, sticky="w")

    headers = ["Marca", "Ano", "Preço", "Região"]
    for col, header in enumerate(headers):
        create_label(cart_frame, text=header, font=("Arial", 12, "bold"), anchor="w").grid(row=1, column=col, padx=10, pady=5, sticky="w")

    for i, wine in enumerate(cart_items):
        create_label(cart_frame, text=wine[1], font=("Arial", 12), anchor="w").grid(row=i + 2, column=0, padx=10, pady=5, sticky="w")
        create_label(cart_frame, text=wine[2], font=("Arial", 12), anchor="center").grid(row=i + 2, column=1, padx=10, pady=5, sticky="w")
        create_label(cart_frame, text=wine[3], font=("Arial", 12), anchor="center").grid(row=i + 2, column=2, padx=10, pady=5, sticky="w")
        create_label(cart_frame, text=wine[4], font=("Arial", 12), anchor="w").grid(row=i + 2, column=3, padx=10, pady=5, sticky="w")

    cart_window.mainloop()


