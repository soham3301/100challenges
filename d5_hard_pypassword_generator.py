import random

# The hard one

# How many letters would you like in your Password?
# How many symbols would you like in your Password?
# How many numbers would you like in your Password?

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("=== WELCOME TO THE PY-PASSWORD-GENERATOR ===")

your_letters = abs(int(input("How many letters would you like in your Password?\n")))
your_numbers = abs(int(input("How many numbers would you like in your Password?\n")))
your_symbols = abs(int(input("How many symbols would you like in yuor Password?\n")))

password_letter = []
password_number = []
password_symbol = []

for _ in range(0, your_letters):
    random_no_for_letters = random.randint(0, len(letters) - 1)
    password_letter.append(letters[random_no_for_letters])

for _ in range(0, your_numbers):
    random_no_for_numbers = random.randint(0, len(numbers) - 1)
    password_number.append(numbers[random_no_for_numbers])

for _ in range(0, your_symbols):
    random_no_for_symbols = random.randint(0, len(symbols) - 1)
    password_symbol.append(symbols[random_no_for_symbols])

final_password_list = []

for _ in range(0, len(password_letter)):
    random_entry = random.randint(0, len(password_letter) - 1)
    final_password_list.append(password_letter[random_entry])
    password_letter.pop(random_entry)

for _ in range(0, len(password_number)):
    random_entry = random.randint(0, len(password_number) - 1)
    final_password_list.append(password_number[random_entry])
    password_number.pop(random_entry)

for _ in range(0, len(password_symbol)):
    random_entry = random.randint(0, len(password_symbol) - 1)
    final_password_list.append(password_symbol[random_entry])
    password_symbol.pop(random_entry)

# random.shuffle() is the easy option
list_length = len(final_password_list)
final_password_mixed = random.sample(final_password_list, k=list_length)

final_password = ""
for char in final_password_mixed:
    final_password = final_password + str(char)

print(f"Your password is: {final_password}")
