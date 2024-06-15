import tkinter as tk
import re

# Function to check password strength
def check_password_strength(password):
    strength = {
        "length": len(password) >= 8,
        "lowercase": bool(re.search("[a-z]", password)),
        "uppercase": bool(re.search("[A-Z]", password)),
        "digit": bool(re.search("[0-9]", password)),
        "special": bool(re.search("[@#$%^&+=]", password))
    }

    score = sum(strength.values())
    
    if score == 5:
        return "Very Strong", strength
    elif score == 4:
        return "Strong", strength
    elif score == 3:
        return "Medium", strength
    else:
        return "Weak", strength

# Function to update the password strength label and criteria display
def update_password_strength(event=None):
    password = password_entry.get()
    strength, criteria = check_password_strength(password)
    
    # Update strength label text and color
    strength_label.config(text=f"Password Strength: {strength}")
    if strength == "Very Strong":
        strength_label.config(fg="green")
    elif strength == "Strong":
        strength_label.config(fg="blue")
    elif strength == "Medium":
        strength_label.config(fg="orange")
    else:
        strength_label.config(fg="red")

    # Update criteria labels
    length_criteria.config(fg="green" if criteria["length"] else "red")
    lowercase_criteria.config(fg="green" if criteria["lowercase"] else "red")
    uppercase_criteria.config(fg="green" if criteria["uppercase"] else "red")
    digit_criteria.config(fg="green" if criteria["digit"] else "red")
    special_criteria.config(fg="green" if criteria["special"] else "red")

# Create the main window
root = tk.Tk()
root.title("Password Strength Tester")

# Create and place the widgets
tk.Label(root, text="Enter Password:").grid(row=0, column=0, padx=10, pady=10)
password_entry = tk.Entry(root, show="*", width=30)
password_entry.grid(row=0, column=1, padx=10, pady=10)
password_entry.bind("<KeyRelease>", update_password_strength)

strength_label = tk.Label(root, text="Password Strength: ")
strength_label.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Criteria labels
tk.Label(root, text="Criteria:").grid(row=2, column=0, columnspan=2)
length_criteria = tk.Label(root, text="At least 8 characters")
length_criteria.grid(row=3, column=0, columnspan=2)
lowercase_criteria = tk.Label(root, text="Contains a lowercase letter")
lowercase_criteria.grid(row=4, column=0, columnspan=2)
uppercase_criteria = tk.Label(root, text="Contains an uppercase letter")
uppercase_criteria.grid(row=5, column=0, columnspan=2)
digit_criteria = tk.Label(root, text="Contains a digit")
digit_criteria.grid(row=6, column=0, columnspan=2)
special_criteria = tk.Label(root, text="Contains a special character (@#$%^&+=)")
special_criteria.grid(row=7, column=0, columnspan=2)

# Start the GUI event loop
root.mainloop()