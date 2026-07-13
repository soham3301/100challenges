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

celeb_copy = celeb_data.copy()

def display_compare_a():
    print("Compare A: Cristiano Ronaldo, a Footballer, from Portugal.")
    return "followers of cr"

def display_compare_b():
    print("Compare B: Rihana, a Musician, from Barbados.")
    return "followers of rh"

def display_board():
    print(higher_lower_logo)
    f1 = display_compare_a()
    print(the_vs_logo)
    f2 = display_compare_b()
    return f1, f2

def ask_user():
    user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()
    return user_choice

def result_calculator(number_of_a, number_of_b, user_choice):
    print(number_of_a, number_of_b, user_choice)
    if user_choice == "a":
        return True
    else:
        return False

def main():
    while True:
        comp_a_number, comp_b_number = display_board()
        user_input = ask_user()
        game_stopper = result_calculator(comp_a_number, comp_b_number, user_input)
        if not game_stopper:
            print("You Lost.")
            break

main()