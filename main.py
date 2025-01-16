import customtkinter as ctk
from utils_tkinter import (
    clear_screen,
    set_widget_style,
    show_info_message,
    show_error_message,
    show_confirmation_message,
    create_label,
    create_button,
    create_entry,
    center_window, table_wines
)
import wines
import db_wines

app = ctk.CTk()
app.title("CustomTkinter Utilities Demo")
center_window(app, 800, 700)

# Create the main application frame
app_frame = ctk.CTkFrame(app)
table_wines(app)

# Start the application
app.mainloop()
