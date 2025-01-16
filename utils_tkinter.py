import customtkinter as ctk
from tkinter import messagebox

def clear_screen(frame: ctk.CTk):
    """
    Remove all widgets from the provided frame or window.
    :param frame: The frame or window whose widgets should be removed.
    :return: None
    """
    for widget in frame.winfo_children():
        widget.destroy()

def set_widget_style(widget, font: tuple = ("Arial", 12), padding: int = 5):
    """
    Apply a common style to a CustomTkinter widget.
    :param widget: The widget to style.
    :param font: Tuple defining the font (name, size, style).
    :param padding: Default padding for the widget.
    :return: None
    """
    widget.configure(font=font, padx=padding, pady=padding)

def show_info_message(title: str, message: str):
    """
    Display an informational message box.
    :param title: The title of the message box.
    :param message: The message to display.
    :return: None
    """
    messagebox.showinfo(title, message)

def show_error_message(title: str, message: str):
    """
    Display an error message box.
    :param title: The title of the message box.
    :param message: The error message to display.
    :return: None
    """
    messagebox.showerror(title, message)

def show_confirmation_message(title: str, message: str) -> bool:
    """
    Display a confirmation dialog and return the user's response.
    :param title: The title of the confirmation dialog.
    :param message: The message to display in the confirmation dialog.
    :return: True if the user confirms, False otherwise.
    """
    return messagebox.askyesno(title, message)

def create_label(parent: ctk.CTk, text: str, font: tuple = ("Arial", 12), anchor: str = "w") -> ctk.CTkLabel:
    """
    Create a CustomTkinter label with common configuration.
    :param parent: The parent widget where the label will be placed.
    :param text: The text to display on the label.
    :param font: Tuple defining the font (name, size, style).
    :param anchor: The anchor position for the text (e.g., 'w', 'center').
    :return: Configured CTkLabel.
    """
    label = ctk.CTkLabel(parent, text=text, font=font, anchor=anchor)
    return label

def create_button(parent: ctk.CTk, text: str, command, font: tuple = ("Arial", 12)) -> ctk.CTkButton:
    """
    Create a CustomTkinter button with common configuration.
    :param parent: The parent widget where the button will be placed.
    :param text: The text to display on the button.
    :param command: The function to execute when the button is clicked.
    :param font: Tuple defining the font (name, size, style).
    :return: Configured CTkButton.
    """
    button = ctk.CTkButton(parent, text=text, command=command, font=font)
    return button

def create_entry(parent: ctk.CTk, placeholder: str = "", font: tuple = ("Arial", 12)) -> ctk.CTkEntry:
    """
    Create a CustomTkinter entry with common configuration.
    :param parent: The parent widget where the entry will be placed.
    :param placeholder: Placeholder text for the entry.
    :param font: Tuple defining the font (name, size, style).
    :return: Configured CTkEntry.
    """
    entry = ctk.CTkEntry(parent, placeholder_text=placeholder, font=font)
    return entry

def center_window(window: ctk.CTk, width: int, height: int):
    """
    Center a tkinter or CustomTkinter window on the screen.
    :param window: The window to center.
    :param width: The width of the window.
    :param height: The height of the window.
    :return: None
    """
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)

    window.geometry(f"{width}x{height}+{x}+{y}")