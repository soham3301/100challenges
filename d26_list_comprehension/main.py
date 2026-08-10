import csv

received_alphabet_data = {}

with open("./nato_alphabet.csv") as file:
    render = csv.reader(file)
    for row in render:
        received_alphabet_data[row[0]] = row[1]

while True:
    user_input = input("Enter a name: ")
    if user_input == "exit":
        break
    else:
        user_input_list = list(user_input)
        result_list = [received_alphabet_data[letter.upper()] for letter in user_input_list]
        print(result_list)