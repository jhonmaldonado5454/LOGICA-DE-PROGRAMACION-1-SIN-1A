# Password Generator

This Python code generates a secure password by meeting certain strength criteria. Here is how the code works:

1. Imports and Function Definitions:
   
import tkinter as tk: Imports the tkinter module and assigns it an alias tk.
from tkinter import messagebox: Imports the messagebox module from tkinter for displaying error messages.

2. Function Definitions:
   
is_strong(password): Checks if the password meets criteria for a strong password (has uppercase, lowercase, digit, and special characters).
generate_password(): Generates a strong password based on user input, updates the GUI label with the generated password, and handles error messages for invalid inputs.

5. tkinter GUI Setup:
window = tk.Tk(): Creates the main tkinter window.
window.title("Password Generator"): Sets the title of the window.
length_label = tk.Label(window, text="Enter Password Length:"): Creates a label widget for prompting the user to enter password length.
length_entry = tk.Entry(window): Creates an entry widget where the user can input the password length.
generate_button = tk.Button(window, text="Generate Password", command=generate_password): Creates a button widget that triggers the generate_password() function when clicked.
password_label = tk.Label(window, text=""): Creates a label widget for displaying the generated password.

6. Widget Packing:
.pack(): Method used to display widgets in the tkinter window. The pady parameter adds vertical padding around each widget to improve spacing and appearance.

Main Loop:
window.mainloop(): Starts the tkinter event loop, which listens for events (like button clicks) and keeps the GUI active and responsive.

