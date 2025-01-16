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
    center_window
)

def on_submit():
    name = entry_name.get()
    if not name.strip():
        show_error_message("Error", "Name cannot be empty!")
    else:
        show_info_message("Success", f"Hello, {name}!")

def on_clear():
    """Clear all widgets on the frame and display a message."""
    if show_confirmation_message("Confirm", "Are you sure you want to clear the screen?"):
        clear_screen(app_frame)

app = ctk.CTk()
app.title("CustomTkinter Utilities Demo")
center_window(app, 400, 300)

# Create the main application frame
app_frame = ctk.CTkFrame(app)
app_frame.pack(fill="both", expand=True, padx=20, pady=20)

# Create and add widgets to the frame
label = create_label(app_frame, text="Enter your name:", font=("Arial", 14))
label.pack(pady=(0, 10))

entry_name = create_entry(app_frame, placeholder="Your Name", font=("Arial", 12))
entry_name.pack(pady=(0, 20))

btn_submit = create_button(app_frame, text="Submit", command=on_submit, font=("Arial", 12))
btn_submit.pack(side="left", padx=(0, 10))

btn_clear = create_button(app_frame, text="Clear Screen", command=on_clear, font=("Arial", 12))
btn_clear.pack(side="left", padx=(10, 0))

# Start the application
app.mainloop()
