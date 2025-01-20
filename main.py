import customtkinter as ctk
from utils_tkinter import (
    clear_screen,
    create_label,
    create_button,
    create_entry,
    show_info_message,
    show_error_message,
    center_window,
    table_wines,
    button_add_wine
)
import sqlite3

app = ctk.CTk()
app.title("Wine Management System")
center_window(app, 800, 700)

app_frame = ctk.CTkFrame(app)
app_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

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
    button_add_wine(app_frame)
    

def show_user_view(user_id):
    clear_screen(app_frame)
    table_wines(app_frame)

# Show login form initially
show_login()

app.mainloop()