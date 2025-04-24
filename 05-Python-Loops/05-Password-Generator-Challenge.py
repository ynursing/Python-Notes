import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
           'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G',
           'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Declare a variable to store the choices
password= ""

# Use range() function along with input to determine max number of
# letters, numbers & symbols allowed
for char in range(1, nr_letters + 1):
    # Declare a variable to store the choices that were made
    random_char = random.choice(letters)
    password += random_char

for symbol in range(1, nr_symbols + 1):
    # Declare a variable to store the choices that were made
    random_symbol = random.choice(symbols)
    password += random_symbol

for num in range(1, nr_numbers + 1):
    # Declare a variable to store the choices that were made
    random_number = random.choice(numbers)
    password += random_number

# To use random.shuffle() function, "password" needs to be
# converted to a list.
password_as_list = list(password)
random.shuffle(password_as_list)
# ".join()" function converts list back to a string
password = "".join(password_as_list)
print(f"Your password is:\n{password}")
