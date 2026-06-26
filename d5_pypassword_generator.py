# The easy one

# How many letters would you like in your Password?
# How many symbols would you like in your Password?
# How many numbers would you like in your Password?

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("=== WELCOME TO THE PY-PASSWORD-GENERATOR ===")

your_letters = int(input("How many letters would you like in your Password?\n"))
your_numbers = int(input("How many numbers would you like in your Password?\n"))
your_symbols = int(input("How many symbols would you like in yuor Password?\n"))

password = ""

for char in range(0, your_letters):
    password += random.choice(letters)

for char in range(0, your_numbers):
    password += str(random.choice(numbers))

for char in range(0, your_symbols):
    password += str(random.choice(symbols))

print(f"Your password is: {password}")