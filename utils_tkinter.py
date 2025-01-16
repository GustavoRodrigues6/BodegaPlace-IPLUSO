import sqlite3

import customtkinter as ctk
from tkinter import messagebox

from manage_wine import get_wines


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


def create_entry(parent: ctk.CTk, placeholder: str = "", font: tuple = ("Arial", 12)) -> ctk.CTkEntry:
    entry = ctk.CTkEntry(parent, placeholder_text=placeholder, font=font)
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
    ctk.CTkLabel(frame_cabecalho, text="Marca", font=("Arial", 12, "bold"), anchor="w", width=140).grid(row=0, column=1, padx=(10, 5), pady=2)
    ctk.CTkLabel(frame_cabecalho, text="Ano", font=("Arial", 12, "bold"), anchor="center", width=50).grid(row=0, column=2, padx=5, pady=2)
    ctk.CTkLabel(frame_cabecalho, text="Preço", font=("Arial", 12, "bold"), anchor="center", width=50).grid(row=0, column=3, padx=5, pady=2)
    ctk.CTkLabel(frame_cabecalho, text="Região", font=("Arial", 12, "bold"), anchor="center", width=82).grid(row=0, column=4, padx=5, pady=2)
    ctk.CTkLabel(frame_cabecalho, text="Descrição", font=("Arial", 12, "bold"), anchor="center", width=82).grid(row=0, column=4, padx=5, pady=2)
    ctk.CTkLabel(frame_cabecalho, text="Nutrição", font=("Arial", 12, "bold"), anchor="center", width=82).grid(row=0, column=4, padx=5, pady=2)
    ctk.CTkLabel(frame_cabecalho, text="Fornecedor", font=("Arial", 12, "bold"), anchor="center", width=82).grid(row=0, column=4, padx=5, pady=2)
    ctk.CTkLabel(frame_cabecalho, text="Stock", font=("Arial", 12, "bold"), anchor="center", width=82).grid(row=0, column=4, padx=5, pady=2)

    frame_tabela = ctk.CTkScrollableFrame(parent, width=350, height=250)
    frame_tabela.pack(pady=(0, 10), padx=10)

    wines = get_wines()
    if wines:
        for i, wine in enumerate(wines):
            ctk.CTkLabel(frame_tabela, text=f"{wine[1]}", anchor="w", width=150).grid(row=i + 1, column=1, padx=5, pady=2)
            ctk.CTkLabel(frame_tabela, text=f"{wine[2]}", anchor="w", width=50).grid(row=i + 1, column=2, padx=5, pady=2)
            ctk.CTkLabel(frame_tabela, text=f"{wine[3]}", anchor="center", width=50).grid(row=i + 1, column=3, padx=5, pady=2)
            ctk.CTkLabel(frame_tabela, text=f"{wine[4]}", anchor="center", width=50).grid(row=i + 1, column=4, padx=5, pady=2)
            ctk.CTkLabel(frame_tabela, text=f"{wine[5]}", anchor="center", width=50).grid(row=i + 1, column=4, padx=5, pady=2)
            ctk.CTkLabel(frame_tabela, text=f"{wine[6]}", anchor="center", width=50).grid(row=i + 1, column=4, padx=5, pady=2)
            ctk.CTkLabel(frame_tabela, text=f"{wine[7]}", anchor="center", width=50).grid(row=i + 1, column=4, padx=5, pady=2)
            ctk.CTkLabel(frame_tabela, text=f"{wine[8]}", anchor="center", width=50).grid(row=i + 1, column=4, padx=5, pady=2)
    else:
        ctk.CTkLabel(frame_tabela, text="Nenhum usuário cadastrado!", font=("Arial", 12), anchor="center").grid(row=1, column=0, columnspan=5, pady=10)
