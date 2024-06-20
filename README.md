# LOGICA-DE-PROGRAMACION-1-SIN-1A

This Python code generates a secure password by meeting certain strength criteria. Here is how the code works:

1. Module import:
 - The `random` module is imported to generate random characters.

2. `is_strong` function:
 - I defined a function called `is_strong` that checks if a password meets the following criteria:
 - At least one capital letter.
 - At least one lowercase letter.
 - At least one digit.
 - At least one special character (from a specific set `!@#$%^&*()`).

3. Request password length:
 - Prompts the user to enter the desired password length.
 - If the length is less than or equal to 3, prompts the user to enter a valid length again (minimum 4).

4. Define possible characters:
 - I defined a string with all possible characters that can be part of the password (`ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()`).

5. Password generation:
 - Used a `for` loop to generate a random password of the specified length, selecting random characters from the string of possible characters.

6. Password verification and regeneration:
 - Used a `while` loop to check if the generated password meets the strength criteria defined by the `is_strong` function.
 - If the password does not meet the criteria, a new password is regenerated until it meets all requirements.

7. Show the generated password:
 - Finally, the generated password that meets all security criteria is printed.

In short, this code generates a strong password that includes uppercase letters, lowercase letters, digits and special characters, thus ensuring its strength and complexity.
