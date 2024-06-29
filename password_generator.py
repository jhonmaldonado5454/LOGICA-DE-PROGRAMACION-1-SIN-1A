import random
import tkinter as tk
from tkinter import messagebox
import pyperclip  # Library to interact with clipboard

# Function to check if the password meets certain criteria
def is_strong(password):
    """Check if the password meets the criteria for a strong password."""
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in "!@#$%^&*()" for c in password)
    return has_upper and has_lower and has_digit and has_special

# Function to generate a strong password
def generate_password():
    """Generate a strong password based on user input."""
    password_length = length_entry.get()  # Read password length from entry field
    try:
        password_length = int(password_length)  # Convert input to integer
        if password_length <= 3:
            # Show error message if password length is less than or equal to 3
            messagebox.showerror("Error", "Minimum length should be 4.")
            return
    except ValueError:
        # Show error message if input is not a valid number
        messagebox.showerror("Error", "Please enter a valid number.")
        return
    
    # Define possible characters for password generation
    possible_characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()"
    password = ""
    
    # Generate password until it meets the criteria for a strong password
    while not is_strong(password):
        password = ""
        for _ in range(password_length):
            # Generate random index to pick characters from possible_characters
            random_index = random.randint(0, len(possible_characters) - 1)
            password += possible_characters[random_index]
    
    # Update label to display the generated password
    password_label.config(text="Generated Password: " + password)
    # Enable copying generated password to clipboard
    copy_button.config(state=tk.NORMAL)

# Function to copy password to clipboard
def copy_password():
    """Copy the generated password to clipboard."""
    generated_password = password_label.cget("text")[18:]  # Extract the password from label text
    pyperclip.copy(generated_password)  # Copy password to clipboard
    messagebox.showinfo("Copied", "Password copied to clipboard!")

# Create tkinter window
window = tk.Tk()
window.title("Password Generator")

# Increase window size
window.geometry("400x300")  # Set initial window size

# Label and Entry for password length
length_label = tk.Label(window, text="Enter Password Length:")
length_label.pack(pady=10)  # Add padding around the label
length_entry = tk.Entry(window)
length_entry.pack()  # Display the entry field for password length

# Button to generate password
generate_button = tk.Button(window, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)  # Add padding around the button

# Label to display generated password
password_label = tk.Label(window, text="")
password_label.pack(pady=10)  # Add padding around the label

# Button to copy password to clipboard
copy_button = tk.Button(window, text="Copy Password", command=copy_password, state=tk.DISABLED)
copy_button.pack(pady=10)  # Add padding around the button

# Run the tkinter main loop
window.mainloop()

