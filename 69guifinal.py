import tkinter as tk
from tkinter import PhotoImage, filedialog
import os
import webbrowser
from PIL import Image, ImageTk

import final3 as final
import time
#####################################################
from tkinter import ttk
import threading




xl11 = "abc"

def login():
    entered_username = username_entry.get()
    entered_password = password_entry.get()

    if entered_username == "u1" and entered_password == "p1":
        login_window.destroy()  # Close the login window
        main_gui()  # Open the main GUI
    else:
        login_status_label.config(text="Invalid username or password")




def progress():

 
    # GUI setup
    root = tk.Tk()
    root.title("BillForge")
    #loading_label = ttk.Label(loading_frame, text="Generating...", font=("Helvetica", 12))
    #loading_label.grid(row=2, column=0, columnspan=2, pady=5)
       
    def simulate_long_running_task():
        # Simulate a long-running task
        #time.sleep(5)
        final.main()

    def start_loading():
        loading_frame.pack()
        # Start a new thread for the long-running task
        threading.Thread(target=simulate_long_running_task, daemon=True).start()
        # Poll the thread to check if it's still running
        root.after(100, check_thread)

    def check_thread():
        #global loading_label
        # Check if the thread is still running
        if threading.active_count() > 1:
            # If the thread is still running, schedule another check
            print("Process Running .....")
            #loading_label = ttk.Label(loading_frame, text="Generating...", font=("Helvetica", 12))
            #loading_label.grid(row=2, column=0, columnspan=2, pady=5)
            root.after(100, check_thread)
        else:
            # If the thread has finished, hide the loading frame
            loading_frame.pack_forget()
            root.destroy()
            
            
            

    # color1 = "#aaffcc"  # Light green
    # color2 = "#aaffcc" 
    # color3 = "#ffffff"
    # #color2 = "#aaffdd"
    # #color2 = "#003366"  # Dark blue

    # # Create a linear gradient
    # for i in range(300):
    #     gradient_color = "#%02x%02x%02x" % (
    #         int((1 - i / 300) * int(color1[1:3], 16) + i / 300 * int(color2[1:3], 16)),
    #         int((1 - i / 300) * int(color1[3:5], 16) + i / 300 * int(color2[3:5], 16)),
    #         int((1 - i / 300) * int(color1[5:], 16) + i / 300 * int(color2[5:], 16))
    #     )

    # root.configure(bg=gradient_color)     
    
    
    
    
    
    

    # Create a frame for the loading spinner with a width of 4 inches
    loading_frame = ttk.Frame(root, width=4*root.winfo_fpixels('1i'))
    loading_label = ttk.Label(loading_frame, text="Bill Generation in progress , please wait...", font=("Helvetica", 12))
    loading_label.grid(row=1, column=0, columnspan=2, pady=5)
    loading_spinner = ttk.Progressbar(loading_frame, mode="indeterminate")
    
    

    loading_label.pack(pady=10)
    loading_spinner.pack()

    #  start the loading process
    start_loading()

    root.mainloop()

# Call the progress function





#progress()






def main_gui():
    # Create the main window
    main_root = tk.Tk()
    main_root.title("BillForge")

    # Background color gradient
    color1 = "#aaffcc"  # Light green
    color2 = "#aaffcc" 
    color3 = "#ffffff"
    #color2 = "#aaffdd"
    #color2 = "#003366"  # Dark blue

    # Create a linear gradient
    for i in range(300):
        gradient_color = "#%02x%02x%02x" % (
            int((1 - i / 300) * int(color1[1:3], 16) + i / 300 * int(color2[1:3], 16)),
            int((1 - i / 300) * int(color1[3:5], 16) + i / 300 * int(color2[3:5], 16)),
            int((1 - i / 300) * int(color1[5:], 16) + i / 300 * int(color2[5:], 16))
        )

    main_root.configure(bg=gradient_color)  # Set background color of the entire window
    
    
# Logo
    try:
       original_logo = Image.open("logo66.png")
       logo_image = ImageTk.PhotoImage(original_logo)
       logo_label = tk.Label(main_root, image=logo_image, bg=color1)
       logo_label.grid(row=0, column=0, columnspan=2, pady=10, padx=10)
    except tk.TclError as e:
       print(f"Error: {e}")
 

    # Functions for main GUI
    def open_doc_dialog():
        doc_file_path = filedialog.askopenfilename(title="Select a .doc File", filetypes=[("Word files", "*.docx")])
        doc_entry_var.set(doc_file_path)
        if doc_file_path:
            doc_file_name = os.path.basename(doc_file_path)
            print(f"Selected .docx File: {doc_file_name}")

    def open_xl_dialog():
        global xl11  # Use the global variable
        xl_file_path = filedialog.askopenfilename(title="Select a .xlsx File", filetypes=[("Excel files", "*.xlsx")])
        xl_entry_var.set(xl_file_path)
        xl11 = xl_file_path  # Update the global variable
        if xl_file_path:
            xl_file_name = os.path.basename(xl_file_path)
            print(f"Selected .xlsx File: {xl_file_name}")

    def open_folder_dialog():
        folder_path = filedialog.askdirectory(title="Select a Folder")
        folder_entry_var.set(folder_path)
        if folder_path:
            print(f"Selected Folder: {folder_path}")

    def edit_email():
        # excel_file_path = "email.xlsx"
        excel_file_path = xl11

        # Check if the file exists before opening
        if os.path.exists(excel_file_path):
            os.system(f'start excel "{excel_file_path}"')
        else:
            print(f"File '{excel_file_path}' not found.")

    def send_email():
        print("Send Email button clicked")

    def generate():
        print("Generate button clicked")
        progress()

        # Perform the main function
        
      
        
        

    # Create and configure widgets for main GUI
    doc_entry_var = tk.StringVar()
    xl_entry_var = tk.StringVar()
    folder_entry_var = tk.StringVar()

    doc_label = tk.Label(main_root, text="Select Bill.docs File:", bg=gradient_color)
    doc_entry = tk.Entry(main_root, textvariable=doc_entry_var, width=50, state='disabled')
    doc_button = tk.Button(main_root, text="Open File", command=open_doc_dialog, bg=color3)

    xl_label = tk.Label(main_root, text="Select Email.xlsx File:", bg=gradient_color)
    xl_entry = tk.Entry(main_root, textvariable=xl_entry_var, width=50, state='disabled')
    xl_button = tk.Button(main_root, text="Open file", command=open_xl_dialog, bg=color3)

    folder_label = tk.Label(main_root, text="Destination Folder:", bg=gradient_color)
    folder_entry = tk.Entry(main_root, textvariable=folder_entry_var, width=50, state='disabled')
    folder_button = tk.Button(main_root, text="Open Folder", command=open_folder_dialog, bg=color3)

    edit_email_button = tk.Button(main_root, text="Edit Email", command=edit_email, bg=color3)
    send_email_button = tk.Button(main_root, text="Send Email", command=send_email, bg=color3)
    generate_button = tk.Button(main_root, text="Generate", command=generate, bg=color3)

    hi_label = tk.Label(main_root, text="BillForge KUET Teachers’ Edition", font=("Helvetica", 12), bg=gradient_color)
    hi_label.grid(row=1, column=0, columnspan=3, pady=5)

    # Grid layout for main GUI
    doc_label.grid(row=2, column=0, padx=10, pady=5)
    doc_entry.grid(row=2, column=1, padx=10, pady=5)
    doc_button.grid(row=2, column=2, padx=10, pady=5)

    xl_label.grid(row=3, column=0, padx=10, pady=5)
    xl_entry.grid(row=3, column=1, padx=10, pady=5)
    xl_button.grid(row=3, column=2, padx=10, pady=5)

    folder_label.grid(row=4, column=0, padx=10, pady=5)
    folder_entry.grid(row=4, column=1, padx=10, pady=5)
    folder_button.grid(row=4, column=2, padx=10, pady=5)

    edit_email_button.grid(row=6, column=0, padx=10, pady=5)
    send_email_button.grid(row=6, column=1, padx=10, pady=5)
    generate_button.grid(row=6, column=2, padx=10, pady=5)

    # Run the main loop for main GUI
    main_root.mainloop()

#main_gui()  # Run the main GUI directly for testing



# Create the login window
login_window = tk.Tk()
login_window.title("BillForge")

# Background color gradient
canvas = tk.Canvas(login_window, width=400, height=300, highlightthickness=0)
canvas.grid(row=0, column=0, rowspan=5, columnspan=2)

color1 = "#aaffcc"  # Light green
color2 = "#aaffcc" 
color3 = "#003366"  # Dark blue
colour4="26CE06"
color5 = "#ffffff"
#gradient_color=color1

# Create a linear gradient
for i in range(300):
    gradient_color = "#%02x%02x%02x" % (
        int((1 - i / 300) * int(color1[1:3], 16) + i / 300 * int(color2[1:3], 16)),
        int((1 - i / 300) * int(color1[3:5], 16) + i / 300 * int(color2[3:5], 16)),
        int((1 - i / 300) * int(color1[5:], 16) + i / 300 * int(color2[5:], 16))
    )
    canvas.create_line(0, i, 400, i, fill=gradient_color, width=1)

# Logo
try:
    original_logo = Image.open("logo5.png")
    logo_image = ImageTk.PhotoImage(original_logo)
    logo_label = tk.Label(login_window, image=logo_image, bg=color1)
    logo_label.grid(row=0, column=0, columnspan=2, pady=10, padx=10)
except tk.TclError as e:
    print(f"Error: {e}")
    
    
hi_kuet_label = tk.Label(login_window, text="Khulna University of Engineering & Technology", font=("Helvetica", 12), bg=gradient_color)
hi_kuet_label.grid(row=1, column=0, columnspan=2, pady=5)

# Create and configure widgets for login window
username_label = tk.Label(login_window, text="Username:", bg=gradient_color)
username_entry = tk.Entry(login_window)
password_label = tk.Label(login_window, text="Password :", bg=gradient_color)
password_entry = tk.Entry(login_window, show="*")
login_button = tk.Button(login_window, text="Login", command=login, bg=color5)
login_status_label = tk.Label(login_window, text="", bg=gradient_color)

# Grid layout for login window
username_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")
username_entry.grid(row=2, column=1, padx=10, pady=5, sticky="w")
password_label.grid(row=3, column=0, padx=10, pady=5, sticky="e")
password_entry.grid(row=3, column=1, padx=10, pady=5, sticky="w")
login_button.grid(row=4, column=0, columnspan=2, pady=10)
login_status_label.grid(row=5, column=0, columnspan=2, pady=5)

# Run the main loop for login window
login_window.mainloop()