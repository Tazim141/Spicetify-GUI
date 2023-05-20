import os
import tkinter as tk
import subprocess

# Get the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

def install_spicetify():
    try:
        exe_path = os.path.join(current_dir, "dependencies/installSpicetify.exe")
        subprocess.Popen(exe_path, shell=True)
    except FileNotFoundError:
        print("installSpicetify.exe not found.")

def uninstall_spicetify():
    try:
        exe_path = os.path.join(current_dir, "dependencies/uninstallSpicetify.exe")
        subprocess.Popen(exe_path, shell=True)
    except FileNotFoundError:
        print("uninstallSpicetify.exe not found.")



# Create the main window
window = tk.Tk()
window.configure(bg="#212121")
window.title("Spicetify")
window.iconbitmap(os.path.join(current_dir, 'dependencies/icon1.ico'))
window.resizable(False, False)  # Disable window resizing

# Set the custom font and size
button_font = ("Helvetica", 12, "bold")

# Create the "Install Spicetify" button
button_install_spicetify = tk.Button(window, text="Install", command=install_spicetify,
                                     font=button_font, bg="#f8be51", fg="#303846", width=20, height=10)
button_install_spicetify.grid(row=0, column=0, padx=5, pady=5)
button_install_spicetify.bind("<Enter>", lambda event: button_install_spicetify.config(bg="#fff36f"))
button_install_spicetify.bind("<Leave>", lambda event: button_install_spicetify.config(bg="#f8be51"))
button_install_spicetify.config(borderwidth=0)

# Create the "Uninstall Spicetify" button
button_uninstall_spicetify = tk.Button(window, text="Uninstall", command=uninstall_spicetify,
                                       font=button_font, bg="#535353", fg="white", width=20, height=10)
button_uninstall_spicetify.grid(row=0, column=1, padx=5, pady=5)
button_uninstall_spicetify.bind("<Enter>", lambda event: button_uninstall_spicetify.config(bg="#b3b3b3"))
button_uninstall_spicetify.bind("<Leave>", lambda event: button_uninstall_spicetify.config(bg="#535353"))
button_uninstall_spicetify.config(borderwidth=0,)

# Start the GUI event loop
window.mainloop()
