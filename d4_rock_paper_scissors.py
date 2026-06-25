import random

# Declaring the variables
# Rock
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
R O C K
"""

# Paper
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
P A P E R
"""

# Scissor
scissor = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
S C I S S O R
"""

print("WELCOME TO /// ROCK = PAPER = SCISSORS ///")

# Creating the user / computer output
decision_list = [rock, paper, scissor]

computer_result = random.choice(decision_list)

your_choice = int(input("Type 0 for 'Rock', Type 1 for 'Paper' and Type 2 for 'Scissor'\n"))
if your_choice == 0 or your_choice == 1 or your_choice == 2:
    your_result = decision_list[your_choice]
    print(f"Your choice is: {your_result}")
    print(f"Computer's choice is: {computer_result}")
    if computer_result == your_result:
        print("It's a DRAW")
    elif computer_result == rock:
        if your_result == paper:
            print("You WIN. Compueter LOOSE")
        else:
            print("You LOOSE. Computer WIN")
    elif computer_result == paper:
        if your_result == rock:
            print("You LOOSE. Computer WIN")
        else:
            print("You WIN. Computer LOOSE")
    else:
        if your_result == rock:
            print("You WIN. Computer LOOSE")
        else:
            print("You LOOSE. Computer WIN")
else:
    your_result = your_choice
    print(f"You entered {your_choice} which is a wrong input!")
print("=== END OF GAME ===")