from tkinter import *
from tkinter import messagebox

def validate_password(password):
    """Validate a password based on predefined criteria."""
    min_length = 8
    special_characters = "@$_&!%"
    l, u, p, d = 0, 0, 0, 0

    if len(password) < min_length:
        return "Invalid Password: Must be at least 8 characters long."

    for char in password:
        if char.islower():
            l += 1
        elif char.isupper():
            u += 1
        elif char.isdigit():
            d += 1
        elif char in special_characters:
            p += 1

    if l < 1:
        return "Invalid Password: Must include at least one lowercase letter."
    if u < 1:
        return "Invalid Password: Must include at least one uppercase letter."
    if p < 1:
        return f"Invalid Password: Must include at least one special character ({special_characters})."
    if d < 1:
        return "Invalid Password: Must include at least one digit."

    return "Valid Password!"

def check_password():
    """Handle the validation when the user clicks the 'Check' button."""
    password = entry.get()
    result = validate_password(password)
    messagebox.showinfo("Password Validation Result", result)

def toggle_password_visibility():
    """Toggle the visibility of the password in the entry widget."""
    if entry.cget("show") == "*":
        entry.config(show="")
        toggle_button.config(text="Hide Password")
    else:
        entry.config(show="*")
        toggle_button.config(text="Show Password")

# Create the main application window
root = Tk()
root.title("This is your basic password validity checker")
root.geometry("500x300")
root.configure(bg="#f7f9fc")

# Add a header label
Label(
    root, 
    text="Password Validity Checker", 
    font=("Arial Bold", 16), 
    fg="#1e88e5", 
    bg="#f7f9fc"
).pack(pady=10)

# Add a description label
Label(
    root, 
    text="Check if your password meets the security criteria.", 
    font=("Arial", 12), 
    fg="#455a64", 
    bg="#f7f9fc"
).pack(pady=5)

# Add an entry widget for password input
entry_frame = Frame(root, bg="#f7f9fc")
entry_frame.pack(pady=20)

Label(entry_frame, text="Enter your password:", font=("Arial", 12), fg="#37474f", bg="#f7f9fc").grid(row=0, column=0, padx=10)
entry = Entry(entry_frame, width=30, show="*", font=("Arial", 12))
entry.grid(row=0, column=1, padx=10)

# Add a toggle button for password visibility
toggle_button = Button(
    root, 
    text="Show Password", 
    command=toggle_password_visibility, 
    font=("Arial", 10), 
    bg="#bbdefb", 
    activebackground="#64b5f6"
)
toggle_button.pack(pady=5)

# Add a button to validate the password
Button(
    root, 
    text="Check Password", 
    command=check_password, 
    font=("Arial", 12), 
    bg="#1e88e5", 
    fg="white", 
    activebackground="#1565c0"
).pack(pady=10)

# Add a footer label
Label(
    root, 
    text="Secure your digital life with strong passwords!", 
    font=("Arial Italic", 10), 
    fg="#607d8b", 
    bg="#f7f9fc"
).pack(side=BOTTOM, pady=10)

# Run the Tkinter main loop
root.mainloop()
