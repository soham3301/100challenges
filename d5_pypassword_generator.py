# The easy one

# How many letters would you like in your Password?
# How many symbols would you like in your Password?
# How many numbers would you like in your Password?

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("=== WELCOME TO THE PY-PASSWORD-GENERATOR ===")

your_letters = int(input("How many letters would you like in your Password?\n"))
your_numbers = int(input("How many numbers would you like in your Password?\n"))
your_symbols = int(input("How many symbols would you like in yuor Password?\n"))

password_letter = []
password_number = []
password_symbol = []

for letter_no in range(0, your_letters):
    password_letter.append(letters[letter_no])

for number_no in range(0, your_numbers):
    password_number.append(numbers[number_no])

for symbol_no in range(0, your_symbols):
    password_symbol.append(symbols[symbol_no])

final_password_list = password_letter + password_number + password_symbol

final_password = ""

for char in final_password_list:
    final_password = final_password + str(char)

print(f"Your password will be: {final_password}")