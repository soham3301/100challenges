with open("../input/names/invalid_names.txt") as name_file:
    for name in name_file:
        the_letter = open("../input/letters/starting_letter.txt", mode="r")
        letter_in_text_form = the_letter.read()
        new_letter = letter_in_text_form.replace("[name]", name.strip())
        new_file = open(f"ready_to_send/letter_for_{name}.txt", mode="w")
        new_file.write(new_letter)
        the_letter.close()
        new_file.close()