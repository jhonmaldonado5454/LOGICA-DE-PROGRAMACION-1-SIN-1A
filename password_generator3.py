import random

# Function to check if the password meets certain criteria
"""A function in programming is a reusable block of code that performs a specific task. 
It takes input, processes it, and returns an output. Functions help organize code, make it more readable, and avoid repetition. 
They can be called (or invoked) multiple times with different inputs to get different results."""
""""""
"""is_strong Function:
The is_strong function checks if the password meets certain criteria to ensure its strength.
has_upper = any(c.isupper() for c in password) checks if there is at least one uppercase letter in the password.
has_lower = any(c.islower() for c in password) checks if there is at least one lowercase letter in the password.
has_digit = any(c.isdigit() for c in password) checks if there is at least one digit in the password.
has_special = any(c in "!@#$%^&*()" for c in the password) checks if there is at least one special character in the password.
The function returns True if all conditions (uppercase, lowercase, digit, and special character) are met, otherwise it returns False."""
def is_strong(password):
    # Check if there is at least one uppercase letter in the password5
    has_upper = any(c.isupper() for c in password)
    # Check if there is at least one lowercase letter in the password
    has_lower = any(c.islower() for c in password)
    # Check if there is at least one digit in the password
    has_digit = any(c.isdigit() for c in password)
    # Check if there is at least one special character in the password
    has_special = any(c in "!@#$%^&*()" for c in password)
    # Return True if all conditions are met
    return has_upper and has_lower and has_digit and has_special

# Request the user to input the desired password length
password_length = int(input("Enter the password length: "))

# Check if the password length is less than 4
while password_length <= 3:
    # If the length is less than or equal to 3, report an error and ask again
    password_length = int(input("Error: Minimum length is 4. Please enter the password length again: "))


# Define the possible characters for the password
possible_characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()"
password = ""

# Generate the password using a for loop
for _ in range(password_length):
    # Generate a random index between 0 and the length of possible_characters minus 1
    random_index = random.randint(0, len(possible_characters) - 1)
    # Add the character at random_index position of possible_characters to the password
    password += possible_characters[random_index]

# Ensure the password meets the criteria, if not, regenerate
"""while Loop:
The while loop ensures the password meets the strength criteria defined in the is_strong function.
The loop condition while not all(is_strong(password)): checks if the password does not meet all criteria. If not, it enters the loop.
Inside the loop:
The password is reset to an empty string.
A new password is generated using a for loop that runs for the specified password length, randomly selecting characters from possible_characters.
The loop continues regenerating the password until it meets all the criteria, ensuring a strong password is generated."""
while not is_strong(password):
    password = ""
    for _ in range(password_length):
        # Generate a random index between 0 and the length of possible_characters minus 1
        random_index = random.randint(0, len(possible_characters) - 1)
        # Add the character at random_index position of possible_characters to the password
        password += possible_characters[random_index]

# Display the generated password
print("The generated password is:", password)
