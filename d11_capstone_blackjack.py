import random
deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
your_deck = []
dealer_deck = []

def want_to_play():
    user_consent = input("Do you want to play a game of BlackJack? Type 'y' or 'n'\n").lower()
    if user_consent == "y":
        blackjack()
        return True
    else:
        print("Thanks for playing with us.")
        return False

def blackjack():
    your_deck.clear()
    dealer_deck.clear()
    your_first_value = your_first_cards()
    dealers_first_value = dealers_first_cards()
    if your_first_value == 21 or dealers_first_value == 21:
        print("IT'S A BLACKJACK")
        winner_calc()
    else:
        game_running = True
        while game_running:
            user_consent = ask_another_card()
            if not user_consent:
                print("Here is your result")
                dealers_cards_addition()
                dealers_final_calculation()
                winner_calc()
                game_running = False
            elif you_over_21() or dealer_over_21():
                winner_calc()
                game_running = False
            else:
                add_another_card()
                if you_over_21():
                    winner_calc()
                    game_running = False
                else:
                    print("Another Card Added to your deck.")
                    dealers_cards_addition()
                    your_current_score_display()
                    dealers_first_card_display()

def your_first_cards():
    first_one = random.choice(deck)
    second_one = random.choice(deck)
    your_deck.append(first_one)
    if second_one == 11:
        the_ace_problem(second_one, your_deck)
    else:
        your_deck.append(second_one)
    your_current_score_display()
    return latest_score(your_deck)

def dealers_first_cards():
    first_one = random.choice(deck)
    second_one = random.choice(deck)
    dealer_deck.append(first_one)
    if second_one == 11:
        the_ace_problem(second_one, dealer_deck)
    else:
        dealer_deck.append(second_one)
    dealers_first_card_display()
    return latest_score(dealer_deck)

def dealers_cards_addition():
    final_score = latest_score(dealer_deck)
    while final_score <= 17:
        dealer_card = random.choice(deck)
        ace_correction(dealer_deck)
        if dealer_card == 11:
            card_value = the_ace_problem(dealer_card, dealer_deck)
            final_score += card_value
        else:
            dealer_deck.append(dealer_card)
            final_score += dealer_card

def dealers_final_calculation():
    players_score = latest_score(your_deck)
    dealers_last_score = latest_score(dealer_deck)
    while players_score < 21 and players_score > dealers_last_score:
        card = random.choice(deck)
        ace_correction(dealer_deck)
        if card == 11:
            new_ace_value = the_ace_problem(card, dealer_deck)
            dealers_last_score += new_ace_value
        else:
            dealer_deck.append(card)
            dealers_last_score += card

def winner_calc():
    your_total = latest_score(your_deck)
    dealer_total = latest_score(dealer_deck)
    if your_total > 21:
        print("Dealer Won - You Gone over 21")
        final_score_display()
    elif dealer_total > 21:
        print("You Won - Dealer gone over 21")
        final_score_display()
    elif your_total > dealer_total:
        print("You Won")
        final_score_display()
    elif dealer_total > your_total:
        print("Dealer Won")
        final_score_display()
    else:
        print("DRAW")
        final_score_display()

def you_over_21():
    your_latest_score = latest_score(your_deck)
    if your_latest_score > 21:
        return True
    else:
        return False

def dealer_over_21():
    dealer_latest_score = latest_score(dealer_deck)
    if dealer_latest_score > 21:
        return True
    else:
        return False

#? ========================================   HELPERS   ==========================================

def dealers_first_card_display():
    print(f"Dealers First Card: {dealer_deck[0]}")

def your_current_score_display():
    current_score = latest_score(your_deck)
    return print(f"Your Cards: {your_deck}, Current Score: {current_score}")

def ask_another_card():
    another_card = input("Type 'y' to get another card, type 'n' to pass.\n").lower()
    if another_card == "y":
        return True
    else:
        return False

def add_another_card():
    card = random.choice(deck)
    ace_correction(your_deck)
    if card == 11:
        the_ace_problem(card, your_deck)
    else:
        your_deck.append(card)

def final_score_display():
    your_final_score = latest_score(your_deck)
    dealers_final_score = latest_score(dealer_deck)
    print(f"Your Final Hand: {your_deck}, Final Score: {your_final_score}")
    print(f"Dealer's Final Hand: {dealer_deck}, Final Score: {dealers_final_score}")

def latest_score(deck):
    return sum(deck)

def the_ace_problem(the_card, the_deck):
    total_value = sum(the_deck) + the_card
    if total_value > 21:
        the_deck.append(1)
        return 1
    else:
        the_deck.append(11)
        return 11

def ace_correction(the_deck):
    if latest_score(the_deck) > 21:
        if 11 in the_deck:
            ace_index = the_deck.index(11)
            the_deck[ace_index] = 1



#! ========================================   MAIN   ==========================================
def main():
    game_running = True
    while game_running:
        game_running = want_to_play()

main()
