import random
words = ['ant', 'bat', 'camel', 'cat', 'crow', 'deer', 'dog', 'eagle', 'ferret', 'goose', 'hawk', 'llama', 'moose', 'mouse', 'otter', 'owl', 'parrot', 'rabbit', 'raven', 'seal', 'sloth', 'tiger', 'turtle', 'wolf', 'zebra']
pics_hang = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

def generate_randoms():
    random_word = random.choice(words)
    random_blanks = "_"
    for _ in range(0, len(random_word) - 1):
        random_blanks += "_"
    return [random_word, random_blanks]

randoms = generate_randoms()
secret_word = randoms[0]
dashes = randoms[1]
user_lives = len(secret_word)
pic_value = (6 - len(secret_word))
print(f"Here is the secret word: {secret_word}")

def user_live_decrease():
    global user_lives
    global pic_value
    user_lives -= 1
    pic_value += 1
    print(f"WRONG GUESS | User Lives Remains: {user_lives}")

def user_guess_input():
    global dashes
    global pic_value
    user_reply = str(input(f"""                                              
    | |                                             
    | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __   
    | '_ \ / _' | '_ \ / _' | '_ ' _ \ / _' | '_ \  
    | | | | (_| | | | | (_| | | | | | | (_| | | | | 
    |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_| 
                        __/ |                      
                       |___/
    {pics_hang[pic_value]}
    
    Word to guess: {dashes}
    Guess a letter: """))        
    return user_reply


#* The main loop
while dashes.count("_") > 0 and user_lives != 0:
    user_guess = user_guess_input()
    if user_guess in secret_word:
        all_indexes = [idx for idx, val in enumerate(secret_word) if val == user_guess]
        if user_guess not in dashes:                                                                #!   <--- Bug 1 | this will not work if there are 3 or more similar chars inside the secret word (e.g. banana)
            print(f"CORRECT GUESS | User Lives Remains: {user_lives}")
            updated_dashes = dashes[:all_indexes[0]] + user_guess + dashes[all_indexes[0] + 1 :]
        else:
            if len(all_indexes) > 1:                                                                #!   <--- Bug 2 | this will not work when 2 chars are in the secret word (e.g. deer)
                print(f"CORRECT GUESS | User Lives Remains: {user_lives}")
                updated_dashes = dashes[:all_indexes[1]] + user_guess + dashes[all_indexes[1] + 1 :]
            else:
                user_live_decrease()
        dashes = updated_dashes
    else:
        user_live_decrease()
else:
    if user_lives == 0:
        print(f"Game OVER. User Lives: {user_lives}")
    else:
        print(f"*** WOW. YOU WON ***")


#TODO Bug Fix Code
"""
while dashes.count("_") > 0 and user_lives != 0:
    user_guess = user_guess_input()
    if user_guess in secret_word:
        all_indexes = [idx for idx, val in enumerate(secret_word) if val == user_guess]
        updated = list(dashes)
        changed = False
        for idx in all_indexes:
            if updated[idx] == "_":
                updated[idx] = user_guess
                changed = True
        if changed:
            print(f"CORRECT GUESS | User Lives Remains: {user_lives}")
            dashes = "".join(updated)
        else:
            user_live_decrease()
    else:
        user_live_decrease()
"""

#! This is an alert comment
#? This is a query comment
#* This is a highlighted comment
#// Thsi is a deleted comment
#TODO This is a to-do comment
