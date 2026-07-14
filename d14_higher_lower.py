import random
#? NOTE:- Only 10 celebrities are added. Real Game contains much more.

#* =======================   GLOBALS   =========================

higher_lower_logo = '''
▗▖ ▗▖▗▄▄▄▖ ▗▄▄▖▗▖ ▗▖▗▄▄▄▖▗▄▄▖     ▗▖    ▗▄▖ ▗▖ ▗▖▗▄▄▄▖▗▄▄▖ 
▐▌ ▐▌  █  ▐▌   ▐▌ ▐▌▐▌   ▐▌ ▐▌    ▐▌   ▐▌ ▐▌▐▌ ▐▌▐▌   ▐▌ ▐▌
▐▛▀▜▌  █  ▐▌▝▜▌▐▛▀▜▌▐▛▀▀▘▐▛▀▚▖    ▐▌   ▐▌ ▐▌▐▌ ▐▌▐▛▀▀▘▐▛▀▚▖
▐▌ ▐▌▗▄█▄▖▝▚▄▞▘▐▌ ▐▌▐▙▄▄▖▐▌ ▐▌    ▐▙▄▄▖▝▚▄▞▘▐▙█▟▌▐▙▄▄▖▐▌ ▐▌
'''

the_vs_logo = '''
▗▖  ▗▖ ▗▄▄▖
▐▌  ▐▌▐▌   
▐▌  ▐▌ ▝▀▚▖
 ▝▚▞▘ ▗▄▄▞▘
  
'''

celeb_data = [
    {
        "name": "Cristiano Ronaldo",
        "follower_count": 671,
        "description": "Footballer",
        "country": "Portugal",
    },
    {
        "name": "Leonel Messi",
        "follower_count": 511,
        "description": "Footballer",
        "country": "Argentina",
    },
    {
        "name": "Selena Gomez",
        "follower_count": 415,
        "description": "Musician",
        "country": "United States",
    },
    {
        "name": "Kylie Jenner",
        "follower_count": 391,
        "description": "Media Personality",
        "country": "United States",
    },
    {
        "name": "Dwayne 'The Rock' Johnson",
        "follower_count": 390,
        "description": "Actor/Wrestler",
        "country": "United States",
    },
    {
        "name": "Ariana Grande",
        "follower_count": 372,
        "description": "Musician / Actress",
        "country": "United States",
    },
    {
        "name": "Kim Kardashian",
        "follower_count": 353,
        "description": "Media Personality",
        "country": "United States",
    },
    {
        "name": "Virat Kohli",
        "follower_count": 275,
        "description": "Cricketer",
        "country": "India",
    },
    {
        "name": "Justin Bieber",
        "follower_count": 295,
        "description": "Musician",
        "country": "Canada",
    },
    {
        "name": "Rihana",
        "follower_count": 146,
        "description": "Musician",
        "country": "Barbados",
    },
]

#* =======================   DISPLAYS   =========================

def display_compare_a(celeb_name):
    celeb_a_followers = celeb_name["follower_count"]
    print(f"Compare A: {celeb_name["name"]}, a {celeb_name["description"]}, from {celeb_name["country"]}.")
    return celeb_a_followers

def display_compare_b(celeb_name):
    celeb_b_followers = celeb_name["follower_count"]
    print(f"Compare B: {celeb_name["name"]}, a {celeb_name["description"]}, from {celeb_name["country"]}.")
    return celeb_b_followers

def display_board(celeb_name_a, celeb_name_b):
    print(higher_lower_logo)
    f1 = display_compare_a(celeb_name_a)
    print(the_vs_logo)
    f2 = display_compare_b(celeb_name_b)
    return f1, f2

#* =======================   CALCULATIONS   =========================

def result_calculator(number_of_a, number_of_b, user_choice):
    if user_choice == "a":
        return calc_helper(number_of_a, number_of_b, user_choice, "a")
    elif user_choice == "b":
        return calc_helper(number_of_b, number_of_a, user_choice, "b")
    else:
        print("Invalid Input | Try Again")
        return True

def calc_helper(comp_a, comp_b, usr_input, comparable):
    if usr_input == comparable:
        user_choosen = comp_a
        if user_choosen > comp_b:
            return True
        else:
            return False

#* =======================   HELPERS   =========================

def celeb_picker(celeb_list, holder_adder):
    celeb_b_new = random.choice(celeb_list)
    holder_adder.append(celeb_b_new)
    celeb_a_new = holder_adder.pop(0)
    celeb_list.remove(celeb_b_new)
    return celeb_a_new, celeb_b_new

def first_celeb_picker(celeb_list, holder_adder):
    celeb_a = random.choice(celeb_list)
    celeb_list.remove(celeb_a)
    celeb_b = random.choice(celeb_list)
    celeb_list.remove(celeb_b)
    holder_adder.append(celeb_b)
    return celeb_a, celeb_b

def ask_user():
    user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()
    return user_choice

def followers_display_for_result(first_celeb, second_celeb):
    if first_celeb["follower_count"] > second_celeb["follower_count"]:
        print(f"{first_celeb["name"]} has {first_celeb["follower_count"]} million followers | {second_celeb["name"]} has only {second_celeb["follower_count"]} million.")
    else:
        print(f"{second_celeb["name"]} has {second_celeb["follower_count"]} million followers | {first_celeb["name"]} has only {first_celeb["follower_count"]} million.")

#! =======================   MAIN   =========================

def main():
    while True:
        celeb_copy = celeb_data.copy()
        celeb_holder = []
        score = -1
        max_attempt = 10
        while True:
            if len(celeb_holder) == 0:
                celeb_for_a, celeb_for_b = first_celeb_picker(celeb_copy, celeb_holder)
            else:
                celeb_for_a, celeb_for_b = celeb_picker(celeb_copy, celeb_holder)
            comp_a_number, comp_b_number = display_board(celeb_for_a, celeb_for_b)
            user_input = ask_user()
            game_stopper = result_calculator(comp_a_number, comp_b_number, user_input)
            score += 1
            max_attempt -= 1
            if not game_stopper:
                print(f"You Lost. Your Final Score: {score}")
                followers_display_for_result(celeb_for_a, celeb_for_b)
                break
            if max_attempt == 0:
                print(f"Thanks for completing the game. You WON.")
                break
        play_again = input("Want to restart the game? Y / N\n").lower() == "y"
        if not play_again:
            print("Thanks for playing The Higher Lower Game. See You.")
            break

main()