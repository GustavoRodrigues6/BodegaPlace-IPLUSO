import sqlite3

import customtkinter as ctk

from manage_wine import insert_wine
from utils_tkinter import (
    clear_screen,
    set_widget_style,
    show_info_message,
    show_error_message,
    show_confirmation_message,
    create_label,
    create_button,
    create_entry,
    center_window, table_wines, button_add_wine
)
import wines
import db_wines

app = ctk.CTk()
app.title("CustomTkinter Utilities Demo")
center_window(app, 800, 700)

app_frame = ctk.CTkFrame(app)
#table_wines(app)
#btn_add_wine = ctk.CTkButton(app, text="Novo vinho", command=lambda: button_add_wine(app))

def novo_vinho():
    input_fields = {}
    labels = ["Brand", "Year", "Price", "Region", "Description", "Nutrition", "Supplier", "Stock"]

    for i, label_text in enumerate(labels):
        ctk.CTkLabel(app, text=f"{label_text}:", font=("Arial", 12), anchor="w").grid(row=i, column=0, padx=10,
                                                                                      pady=5, sticky="w")
        entry = create_entry(app)
        entry.grid(row=i, column=1, padx=10, pady=5, sticky="w")
        input_fields[label_text] = entry

    def handle_add_wine():
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
            clear_screen(app)
        except ValueError:
            show_error_message("Error", "Invalid input. Please check your entries.")
        except sqlite3.Error as e:
            show_error_message("Database Error", f"An error occurred: {e}")

    submit_button = create_button(app, text="Add Wine", command=handle_add_wine)
    submit_button.grid(row=len(labels), column=0, columnspan=2, pady=10)

new_wine = create_button(app, text="Novo vinho", command=novo_vinho)

app_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
app.mainloop()
