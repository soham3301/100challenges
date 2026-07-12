import random
deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def want_to_play():
    user_consent = input("Do you want to play a game of BlackJack? Type 'y' or 'n'\n").lower()
    if user_consent == "y":
        blackjack()
        return True
    else:
        print("Thanks for playing with us.")
        return False

def blackjack():
    print("Your Cards: [5, 9], Current Score: 14")
    print("Computers First Card: 8")
    while True:
        another_card = input("Type 'y' to get another card, type 'n' to pass.").lower()
        if another_card == "n":
            print("Your Final Hand: [5, 9], Final Score: 14")
            print("Computer's Final Hand: [8, 3, 7], Final Score: 18")
            print("Computer WON")
            break
        else:
            print("ANOTHER CARD GIVEN")



def main():
    game_running = True
    while game_running:
        game_running = want_to_play()

main()
