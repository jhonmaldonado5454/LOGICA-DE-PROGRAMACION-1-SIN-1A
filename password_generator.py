import random

# Solicitar al usuario la longitud de la contraseña
password_length = int(input("Enter the password length: "))

# Definir los caracteres posibles para la contraseña
possible_characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()"
password = ""

# Generar la contraseña, 
#Variable de Control: "i" se utiliza como variable de control del bucle. 
#En este caso, "i" es una convención en Python que indica que la variable no se usará dentro del bucle.
for i in range(password_length):
    # Generar un índice aleatorio entre 0 y la longitud de possible_characters menos 1
    random_index = random.randint(0, len(possible_characters) - 1)
    
    # Añadir el carácter en la posición random_index de possible_characters a la contraseña
    password += possible_characters[random_index]

# Mostrar la contraseña generada
print("The generated password is:", password)
