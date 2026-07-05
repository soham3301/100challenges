# 1. type 'encode' to encrypt, 'decode' to decrypt.
# 2. if 'encode' then --->
# 3. type your messege (without space).
# 4. type the shift number. (shift goes right hand side)
# 5. display the encoded messege.
# 6. ask user to try it again or not.
# 7. same way decode works. in decode the shift goes left hand side.

letters_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encode_or_decode():
    return str(input("Type 'encode' to encrypt, 'decode' to decrypt: ")).lower()

def getting_the_message_and_shift_number():
    the_message = str(input("Type your message (without spaces): ")).lower()
    the_shift_number = int(input("Enter the shift number: "))
    return the_message, the_shift_number

def message_encoding_and_decoding(received_message, shift_number):
    the_message_as_list = list(received_message)
    coded_message_list = []
    coded_message = ""
    for chars in the_message_as_list:
        the_shift_index = letters_list.index(chars) + shift_number
        if the_shift_index >= 26:
            coded_message_list.append(letters_list[the_shift_index - 26])
        elif the_shift_index < 0:
            coded_message_list.append(letters_list[the_shift_index + 26])
        else:
            coded_message_list.append(letters_list[the_shift_index])
    coded_message = "".join(coded_message_list)
    return coded_message

def display_mutated_message(mutated_message, encode_or_decode):
    print(f"Here is your {encode_or_decode} message: {mutated_message}")

def program_continues():
    user_consent = str(input("Type 'Y' to continue, type 'N' to stop: ")).lower()
    if user_consent != "y":
        print("Thanks for using the Caesar Ciphar")
        return False
    else:
        return True

def main():
    program_stopper = True
    while program_stopper:
        user_choice = encode_or_decode()
        if user_choice in ['encode', 'decode']:
            the_message, the_shift_number = getting_the_message_and_shift_number()
            if user_choice == 'encode':
                encoded_message = message_encoding_and_decoding(the_message, the_shift_number)
                display_mutated_message(encoded_message, "encoded")
            elif user_choice == 'decode':
                the_shift_number = -the_shift_number
                decoded_message = message_encoding_and_decoding(the_message, the_shift_number)
                display_mutated_message(decoded_message, "decoded")
        else:
            print("Wrong Input.")
        program_stopper = program_continues()

main()
