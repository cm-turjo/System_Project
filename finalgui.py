import tkinter as tk
from tkinter import filedialog
import os
import webbrowser

def login():
    entered_username = username_entry.get()
    entered_password = password_entry.get()

    if entered_username == "u1" and entered_password == "p1":
        login_window.destroy()  # Close the login window
        main_gui()  # Open the main GUI
    else:
        login_status_label.config(text="Invalid username or password")

def main_gui():
    # Create the main window
    main_root = tk.Tk()
    main_root.title("File and Folder Picker")

    # Functions for main GUI
    def open_doc_dialog():
        doc_file_path = filedialog.askopenfilename(title="Select a .doc File", filetypes=[("Word files", "*.docx")])
        doc_entry_var.set(doc_file_path)
        if doc_file_path:
            doc_file_name = os.path.basename(doc_file_path)
            print(f"Selected .docx File: {doc_file_name}")

    def open_xl_dialog():
        xl_file_path = filedialog.askopenfilename(title="Select a .xlsx File", filetypes=[("Excel files", "*.xlsx")])
        xl_entry_var.set(xl_file_path)
        if xl_file_path:
            xl_file_name = os.path.basename(xl_file_path)
            print(f"Selected .xlsx File: {xl_file_name}")

    def open_folder_dialog():
        folder_path = filedialog.askdirectory(title="Select a Folder")
        folder_entry_var.set(folder_path)
        if folder_path:
            print(f"Selected Folder: {folder_path}")

    def edit_email():
        webbrowser.open("email.xlsx")

    def send_email():
        print("Send Email button clicked")

    def generate():
        print("Generate button clicked")

    # Create and configure widgets for main GUI
    doc_entry_var = tk.StringVar()
    xl_entry_var = tk.StringVar()
    folder_entry_var = tk.StringVar()

    doc_label = tk.Label(main_root, text=".doc File:")
    doc_entry = tk.Entry(main_root, textvariable=doc_entry_var, width=50, state='disabled')
    doc_button = tk.Button(main_root, text="Open .doc Picker", command=open_doc_dialog)

    xl_label = tk.Label(main_root, text=".xlsx File:")
    xl_entry = tk.Entry(main_root, textvariable=xl_entry_var, width=50, state='disabled')
    xl_button = tk.Button(main_root, text="Open .xlsx Picker", command=open_xl_dialog)

    folder_label = tk.Label(main_root, text="Folder:")
    folder_entry = tk.Entry(main_root, textvariable=folder_entry_var, width=50, state='disabled')
    folder_button = tk.Button(main_root, text="Open Folder Picker", command=open_folder_dialog)

    edit_email_button = tk.Button(main_root, text="Edit Email", command=edit_email)
    send_email_button = tk.Button(main_root, text="Send Email", command=send_email)
    generate_button = tk.Button(main_root, text="Generate", command=generate)

    # Grid layout for main GUI
    doc_label.grid(row=0, column=0, padx=10, pady=10)
    doc_entry.grid(row=0, column=1, padx=10, pady=10)
    doc_button.grid(row=0, column=2, padx=10, pady=10)

    xl_label.grid(row=1, column=0, padx=10, pady=10)
    xl_entry.grid(row=1, column=1, padx=10, pady=10)
    xl_button.grid(row=1, column=2, padx=10, pady=10)

    folder_label.grid(row=2, column=0, padx=10, pady=10)
    folder_entry.grid(row=2, column=1, padx=10, pady=10)
    folder_button.grid(row=2, column=2, padx=10, pady=10)

    edit_email_button.grid(row=3, column=0, padx=10, pady=10)
    send_email_button.grid(row=3, column=1, padx=10, pady=10)
    generate_button.grid(row=3, column=2, padx=10, pady=10)

    # Run the main loop for main GUI
    main_root.mainloop()

# Create the login window
login_window = tk.Tk()
login_window.title("Login")

# Create and configure widgets for login window
username_label = tk.Label(login_window, text="Username:")
username_entry = tk.Entry(login_window)
password_label = tk.Label(login_window, text="Password:")
password_entry = tk.Entry(login_window, show="*")
login_button = tk.Button(login_window, text="Login", command=login)
login_status_label = tk.Label(login_window, text="")

# Grid layout for login window
username_label.grid(row=0, column=0, padx=10, pady=10)
username_entry.grid(row=0, column=1, padx=10, pady=10)
password_label.grid(row=1, column=0, padx=10, pady=10)
password_entry.grid(row=1, column=1, padx=10, pady=10)
login_button.grid(row=2, column=0, columnspan=2, pady=10)
login_status_label.grid(row=3, column=0, columnspan=2, pady=10)

# Run the main loop for login window
login_window.mainloop()
