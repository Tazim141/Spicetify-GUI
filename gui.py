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
        print("Spicetify install executable not found.")

def uninstall_spicetify():
    try:
        exe_path = os.path.join(current_dir, "dependencies/uninstallSpicetify.exe")
        subprocess.Popen(exe_path, shell=True)
    except FileNotFoundError:
        print("Spicetify uninstall executable not found.")



# Create the main window
window = tk.Tk()
window.configure(bg="yellow")
window.title("No ads Spotify")
window.iconbitmap(os.path.join(current_dir, 'dependencies/icon.ico'))
window.resizable(False, False)  # Disable window resizing

# Set the custom font and size
button_font = ("Helvetica", 12, "bold")

# Create the "Install Spicetify" button
button_install_spicetify = tk.Button(window, text="Install Spicetify", command=install_spicetify,
                                     font=button_font, bg="green", fg="white", width=20, height=10)
button_install_spicetify.grid(row=0, column=0, padx=5, pady=5)
button_install_spicetify.bind("<Enter>", lambda event: button_install_spicetify.config(bg="dark green"))
button_install_spicetify.bind("<Leave>", lambda event: button_install_spicetify.config(bg="green"))

# Create the "Uninstall Spicetify" button
button_uninstall_spicetify = tk.Button(window, text="Uninstall Spicetify", command=uninstall_spicetify,
                                       font=button_font, bg="red", fg="white", width=20, height=10)
button_uninstall_spicetify.grid(row=0, column=1, padx=5, pady=5)
button_uninstall_spicetify.bind("<Enter>", lambda event: button_uninstall_spicetify.config(bg="dark red"))
button_uninstall_spicetify.bind("<Leave>", lambda event: button_uninstall_spicetify.config(bg="red"))


# Start the GUI event loop
window.mainloop()
