import tkinter as tk
from tkinter import filedialog


def RUN():
    print("ADD Code--------------------------------------------------")
    
    

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
    main_root.title("Exam Information")

    # Functions for main GUI
    def open_file_dialog():
        file_path = filedialog.askopenfilename(title="Select a Document", filetypes=[("Word files", ".docx;.doc")])
        entry_var.set(file_path)
        if file_path:
            file_name = file_path.split("/")[-1]  # Extracting the file name from the path
            print(f"Selected File: {file_name}")

    def show_exam_info():
        exam_year = exam_year_var.get()
        exam_type = exam_type_var.get()
        year = year_var.get()
        term = term_var.get()
        department = department_var.get()
        session = session_var.get()
        file_path = entry_var.get()
        
        
        RUN()

        # Display information in console
        print(f"Exam Year: {exam_year}")
        print(f"Exam Type: {exam_type}")
        print(f"Year: {year}")
        print(f"Term: {term}")
        print(f"Department: {department}")
        print(f"Session: {session}")
        print(f"File Path: {file_path}")

    # Create and configure widgets for main GUI
    exam_year_var = tk.StringVar()
    exam_type_var = tk.StringVar()
    year_var = tk.StringVar()
    term_var = tk.StringVar()
    department_var = tk.StringVar()
    session_var = tk.StringVar()
    entry_var = tk.StringVar()

    exam_year_label = tk.Label(main_root, text="Exam Year:")
    exam_year_entry = tk.Entry(main_root, textvariable=exam_year_var)

    exam_type_label = tk.Label(main_root, text="Exam Type:")
    exam_type_dropdown = tk.OptionMenu(main_root, exam_type_var, "Regular", "Backlog", "Special_Backlog")

    year_label = tk.Label(main_root, text="Year:")
    year_entry = tk.Entry(main_root, textvariable=year_var)

    term_label = tk.Label(main_root, text="Term:")
    term_entry = tk.Entry(main_root, textvariable=term_var)

    department_label = tk.Label(main_root, text="Department:")
    department_entry = tk.Entry(main_root, textvariable=department_var)

    session_label = tk.Label(main_root, text="Session:")
    session_entry = tk.Entry(main_root, textvariable=session_var)

    file_label = tk.Label(main_root, text="File Path:")
    file_entry = tk.Entry(main_root, textvariable=entry_var, width=50, state='disabled')

    file_button = tk.Button(main_root, text="Open Document", command=open_file_dialog)

    show_info_button = tk.Button(main_root, text="Show Exam Info", command=show_exam_info)

    # Grid layout for main GUI
    exam_year_label.grid(row=0, column=0, padx=10, pady=10)
    exam_year_entry.grid(row=0, column=1, padx=10, pady=10)

    exam_type_label.grid(row=1, column=0, padx=10, pady=10)
    exam_type_dropdown.grid(row=1, column=1, padx=10, pady=10)

    year_label.grid(row=2, column=0, padx=10, pady=10)
    year_entry.grid(row=2, column=1, padx=10, pady=10)

    term_label.grid(row=3, column=0, padx=10, pady=10)
    term_entry.grid(row=3, column=1, padx=10, pady=10)

    department_label.grid(row=4, column=0, padx=10, pady=10)
    department_entry.grid(row=4, column=1, padx=10, pady=10)

    session_label.grid(row=5, column=0, padx=10, pady=10)
    session_entry.grid(row=5, column=1, padx=10, pady=10)

    file_label.grid(row=6, column=0, padx=10, pady=10)
    file_entry.grid(row=6, column=1, padx=10, pady=10)
    file_button.grid(row=6, column=2, padx=10, pady=10)

    show_info_button.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

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