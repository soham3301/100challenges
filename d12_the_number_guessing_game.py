import random

def game_mode_selector():
    game_mode = input(f'''
Welcome to the Number Guessing Game
I am thinking a number between 1 and 100
Choose a difficulty, type 'easy' or 'hard': ''').lower()
    if game_mode == "easy":
        return 10
    elif game_mode == "hard":
        return 5
    else:
        return 0

def the_game(level):
    total_attempts = level
    if total_attempts == 0:
        print("Invalid Input | Game Difficulty Selection")
    else:
        game_start(total_attempts)

def game_start(attempts):
    max_attempts = attempts
    the_result = random.randint(1, 100)
    game_runner = True
    while max_attempts > 0 and game_runner:
        try:
            user_input_number = int(input(f"You have {max_attempts} attempts remaining to guess the number\n"))
            if user_input_number >= 1 and user_input_number <= 100:
                game_runner = calculation(user_input_number, the_result)
                max_attempts -= 1
            else:
                max_attempts -= 1
                print(f"Please choose a number in between 1 and 100.")
        except ValueError:
            max_attempts -= 1
            print(f"Invalid Input | Please choose a number.")
    if max_attempts == 0 and game_runner:
        print(f"{max_attempts} attempt left. Game Over. The result was {the_result}")

def calculation(user_input, the_number):
    if user_input == the_number:
        print(f"You Found It. The answer is {the_number}")
        return False
    elif user_input > the_number:
        print("Too High, Guess Again")
        return True
    else:
        print("Too Low, Guess Again")
        return True

def main():
    game_running = True
    while game_running:
        difficulty_level = game_mode_selector()
        the_game(difficulty_level)
        game_running = input("Play Again? Y / N\n").lower() == "y"
        if not game_running:
            print("Thanks for playing The Number Guessing Game. See You.")

main()
