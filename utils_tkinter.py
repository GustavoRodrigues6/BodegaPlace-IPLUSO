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

def table_wines(parent: ctk.CTk):
    frame_cabecalho = ctk.CTkFrame(parent, width=500, height=30)
    frame_cabecalho.pack(pady=(10, 0), padx=10)
    ctk.CTkLabel(frame_cabecalho, text="Marca", font=("Arial", 12, "bold"), anchor="w", width=150).grid(row=0, column=1, padx=(10, 5), pady=2)
    ctk.CTkLabel(frame_cabecalho, text="Ano", font=("Arial", 12, "bold"), anchor="center", width=50).grid(row=0, column=2, padx=5, pady=2)
    ctk.CTkLabel(frame_cabecalho, text="Preço", font=("Arial", 12, "bold"), anchor="center", width=50).grid(row=0, column=3, padx=5, pady=2)
    ctk.CTkLabel(frame_cabecalho, text="Região", font=("Arial", 12, "bold"), anchor="w", width=120).grid(row=0, column=4, padx=5, pady=2)

    frame_tabela = ctk.CTkScrollableFrame(parent, width=450, height=250)
    frame_tabela.pack(pady=(0, 10), padx=10)

    wines = get_wines()
    if wines:
        for i, wine in enumerate(wines):
            ctk.CTkLabel(frame_tabela, text=f"{wine[1]}", anchor="w", width=150).grid(row=i + 1, column=1, padx=5, pady=2)
            ctk.CTkLabel(frame_tabela, text=f"{wine[2]}", anchor="center", width=50).grid(row=i + 1, column=2, padx=5, pady=2)
            ctk.CTkLabel(frame_tabela, text=f"{wine[3]}", anchor="center", width=50).grid(row=i + 1, column=3, padx=5, pady=2)
            ctk.CTkLabel(frame_tabela, text=f"{wine[4]}", anchor="w", width=120).grid(row=i + 1, column=4, padx=5, pady=2)
    else:
        ctk.CTkLabel(frame_tabela, text="Nenhum vinho cadastrado!", font=("Arial", 12), anchor="center").grid(row=1, column=0, columnspan=5, pady=10)

def button_add_wine(parent: ctk.CTk):
    input_fields = {}
    labels = ["Brand", "Year", "Price", "Region", "Description", "Nutrition", "Supplier", "Stock"]

    for i, label_text in enumerate(labels):
        ctk.CTkLabel(parent, text=f"{label_text}:", font=("Arial", 12), anchor="w").grid(row=i, column=0, padx=10, pady=5, sticky="w")
        entry = create_entry(parent)
        entry.grid(row=i, column=1, padx=10, pady=5, sticky="w")
        input_fields[label_text] = entry

    def submit_wine():
        try:
            brand = input_fields["Brand"].get()
            year = int(input_fields["Year"].get())
            price = float(input_fields["Price"].get())
            region = input_fields["Region"].get()
            description = input_fields["Description"].get()
            nutrition = float(input_fields["Nutrition"].get())
            supplier = int(input_fields["Supplier"].get())
            stock = int(input_fields["Stock"].get())
            insert_wine(brand, year, price, region, description, nutrition, supplier, stock)
            show_info_message("Success", "Wine added successfully!")
            clear_screen(parent)
        except ValueError:
            show_error_message("Error", "Invalid input. Please check your entries.")
        except sqlite3.Error as e:
            show_error_message("Database Error", f"An error occurred: {e}")

    submit_button = create_button(parent, text="Add Wine", command=submit_wine, font=("Arial", 12))
    submit_button.grid(row=len(labels), column=0, columnspan=2, pady=10)