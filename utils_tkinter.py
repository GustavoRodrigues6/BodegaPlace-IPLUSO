import customtkinter as ctk
from utils_tkinter import *
import sqlite3
from utils import center_window, show_info_message, show_error_message
from manage_wine import get_wines, insert_wine

app = ctk.CTk()
app.title("Wine Management System")
center_window(app, 800, 700)

app_frame = ctk.CTkFrame(app)
app_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

cart = []

def clear_screen(frame):
    for widget in frame.winfo_children():
        widget.destroy()

def create_label(parent, text, font=("Arial", 12), anchor="w"):
    return ctk.CTkLabel(parent, text=text, font=font, anchor=anchor)

def create_button(parent, text, command, font=("Arial", 12)):
    return ctk.CTkButton(parent, text=text, command=command, font=font)

def create_entry(parent, show=None):
    return ctk.CTkEntry(parent, show=show)

def register_user():
    clear_screen(app_frame)
    input_fields = {}
    labels = ["Username", "Email", "Password", "Address1", "Address2", "NIF"]

    for i, label_text in enumerate(labels):
        create_label(app_frame, text=f"{label_text}:", font=("Arial", 12), anchor="w").grid(row=i, column=0, padx=10, pady=5, sticky="w")
        entry = create_entry(app_frame)
        entry.grid(row=i, column=1, padx=10, pady=5, sticky="w")
        input_fields[label_text] = entry

    def submit_registration():
        username = input_fields["Username"].get()
        email = input_fields["Email"].get()
        password = input_fields["Password"].get()
        address1 = input_fields["Address1"].get()
        address2 = input_fields["Address2"].get()
        nif = input_fields["NIF"].get()

        try:
            connection = sqlite3.connect('users.db')
            cursor = connection.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT NOT NULL,
                    email TEXT NOT NULL UNIQUE,
                    password TEXT NOT NULL,
                    address1 TEXT,
                    address2 TEXT,
                    nif TEXT,
                    is_admin INTEGER NOT NULL
                )
            ''')
            cursor.execute('''
                INSERT INTO users (username, email, password, address1, address2, nif, is_admin)
                VALUES (?, ?, ?, ?, ?, ?, 0)
            ''', (username, email, password, address1, address2, nif))
            connection.commit()
            connection.close()
            show_info_message("Success", "User registered successfully!")
            show_login()
        except sqlite3.IntegrityError:
            show_error_message("Error", "Email already exists.")
        except Exception as e:
            show_error_message("Error", f"An error occurred: {e}")

    submit_button = create_button(app_frame, text="Register", command=submit_registration, font=("Arial", 12))
    submit_button.grid(row=len(labels), column=0, columnspan=2, pady=10)

def show_login():
    clear_screen(app_frame)
    create_label(app_frame, text="Username:", font=("Arial", 12), anchor="w").grid(row=0, column=0, padx=10, pady=5, sticky="w")
    username_entry = create_entry(app_frame)
    username_entry.grid(row=0, column=1, padx=10, pady=5, sticky="w")

    create_label(app_frame, text="Password:", font=("Arial", 12), anchor="w").grid(row=1, column=0, padx=10, pady=5, sticky="w")
    password_entry = create_entry(app_frame, show="*")
    password_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")

    def login():
        username = username_entry.get()
        password = password_entry.get()

        connection = sqlite3.connect('users.db')
        cursor = connection.cursor()
        cursor.execute('SELECT id, is_admin FROM users WHERE username = ? AND password = ?', (username, password))
        user = cursor.fetchone()
        connection.close()

        if user:
            user_id, is_admin = user
            if is_admin:
                show_admin_view(user_id)
            else:
                show_user_view(user_id)
        else:
            show_error_message("Login Failed", "Invalid username or password")

    login_button = create_button(app_frame, text="Login", command=login, font=("Arial", 12))
    login_button.grid(row=2, column=0, columnspan=2, pady=10)

    register_button = create_button(app_frame, text="Register", command=register_user, font=("Arial", 12))
    register_button.grid(row=3, column=0, columnspan=2, pady=10)

def show_admin_view(user_id):
    clear_screen(app_frame)
    table_wines_admin(app_frame)
    add_wine_form(app_frame)

def add_wine_form(parent):
    input_fields = {}
    labels = ["Brand", "Year", "Price", "Region", "Description", "Nutrition", "Supplier", "Stock"]

    for i, label_text in enumerate(labels):
        create_label(parent, text=f"{label_text}:", font=("Arial", 12), anchor="w").grid(row=i + 10, column=0, padx=10, pady=5, sticky="w")
        entry = create_entry(parent)
        entry.grid(row=i + 10, column=1, padx=10, pady=5, sticky="w")
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
            show_admin_view(None)
        except ValueError:
            show_error_message("Error", "Invalid input. Please check your entries.")
        except sqlite3.Error as e:
            show_error_message("Database Error", f"An error occurred: {e}")

    submit_button = create_button(parent, text="Add Wine", command=submit_wine, font=("Arial", 12))
    submit_button.grid(row=len(labels) + 10, column=0, columnspan=2, pady=10)

    submit_button = create_button(parent, text="Analyze", command=Analyse_sales, font=("Arial", 12))
    submit_button.grid(row=len(labels) + 10, column=1, columnspan=3, pady=10)

def Analyse_sales():
    analyse = ctk.CTk()
    analyse.title("Analyse Sales")
    center_window(analyse, 800, 700)

    analyse_frame = ctk.CTkFrame(analyse)
    analyse_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
    create_label(analyse_frame, text="Sales Analysis", font=("Arial", 16), anchor="w").grid(row=0, column=0, padx=10, pady=5, sticky="w")

    headers = ["ID", "Month", "Year", "Sales Value"]
    for col, header in enumerate(headers):
        create_label(analyse_frame, text=header, font=("Arial", 12, "bold"), anchor="w").grid(row=1, column=col, padx=10, pady=5, sticky="w")

    connection = sqlite3.connect('sales.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM monthly_sales')
    sales = cursor.fetchall()
    connection.close()

    total_sales = 0
    for i, sale in enumerate(sales):
        for j, value in enumerate(sale):
            create_label(analyse_frame, text=str(value), font=("Arial", 12), anchor="w").grid(row=i + 2, column=j, padx=10, pady=5, sticky="w")
        total_sales += sale[3]

    create_label(analyse_frame, text=f"Total Sales: ${total_sales:.2f}", font=("Arial", 12, "bold"), anchor="w").grid(row=len(sales) + 2, column=0, padx=10, pady=5, sticky="w", columnspan=4)

    analyse.mainloop()

def search_wines(user_id):
    search_frame = ctk.CTkFrame(app_frame)
    search_frame.grid(row=0, column=0, padx=10, pady=5, sticky="w")

    search_entry = create_entry(search_frame)
    search_entry.grid(row=0, column=0, padx=10, pady=5, sticky="w")

    search_button = create_button(search_frame, text="Search", command=lambda: search_wines_results(app_frame, search_entry.get()), font=("Arial", 12))
    search_button.grid(row=0, column=1, padx=10, pady=5, sticky="w")

    buy_button = create_button(search_frame, text="Buy", command=lambda: buy_wine(search_entry.get(), user_id), font=("Arial", 12))
    buy_button.grid(row=0, column=2, padx=10, pady=5, sticky="w")

    cart_button = create_button(search_frame, text="Cart", command=lambda: show_cart(user_id), font=("Arial", 12))
    cart_button.grid(row=0, column=3, padx=10, pady=5, sticky="w")

def show_user_view(user_id):
    clear_screen(app_frame)
    search_wines(user_id)
    table_wines_user(app_frame)
    create_button(app_frame, text="Edit Account", command=lambda: edit_account(user_id), font=("Arial", 12)).grid(row=3, column=0, padx=10, pady=5, sticky="w")
    create_button(app_frame, text="Delete Account", command=lambda: delete_account(user_id), font=("Arial", 12)).grid(row=3, column=1, padx=10, pady=5, sticky="w")

def edit_account(user_id):
    clear_screen(app_frame)
    input_fields = {}
    labels = ["Username", "Email", "Password", "Address1", "Address2", "NIF"]

    connection = sqlite3.connect('users.db')
    cursor = connection.cursor()
    cursor.execute('SELECT username, email, password, address1, address2, nif FROM users WHERE id = ?', (user_id,))
    user_data = cursor.fetchone()
    connection.close()

    for i, label_text in enumerate(labels):
        create_label(app_frame, text=f"{label_text}:", font=("Arial", 12), anchor="w").grid(row=i, column=0, padx=10, pady=5, sticky="w")
        entry = create_entry(app_frame)
        entry.grid(row=i, column=1, padx=10, pady=5, sticky="w")
        entry.insert(0, user_data[i])
        input_fields[label_text] = entry

    def submit_edit():
        username = input_fields["Username"].get()
        email = input_fields["Email"].get()
        password = input_fields["Password"].get()
        address1 = input_fields["Address1"].get()
        address2 = input_fields["Address2"].get()
        nif = input_fields["NIF"].get()

        try:
            connection = sqlite3.connect('users.db')
            cursor = connection.cursor()
            cursor.execute('''
                UPDATE users
                SET username = ?, email = ?, password = ?, address1 = ?, address2 = ?, nif = ?
                WHERE id = ?
            ''', (username, email, password, address1, address2, nif, user_id))
            connection.commit()
            connection.close()
            show_info_message("Success", "Account updated successfully!")
            show_user_view(user_id)
        except sqlite3.IntegrityError:
            show_error_message("Error", "Email already exists.")
        except Exception as e:
            show_error_message("Error", f"An error occurred: {e}")

    submit_button = create_button(app_frame, text="Save Changes", command=submit_edit, font=("Arial", 12))
    submit_button.grid(row=len(labels), column=0, columnspan=2, pady=10)

def delete_account(user_id):
    def confirm_delete():
        try:
            connection = sqlite3.connect('users.db')
            cursor = connection.cursor()
            cursor.execute('DELETE FROM users WHERE id = ?', (user_id,))
            connection.commit()
            connection.close()
            show_info_message("Success", "Account deleted successfully!")
            show_login()
        except Exception as e:
            show_error_message("Error", f"An error occurred: {e}")

    if show_confirmation_message("Delete Account", "Are you sure you want to delete your account?"):
        confirm_delete()

show_login()

app.mainloop()