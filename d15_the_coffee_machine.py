# 3 Flavours - espresso, latte, cappuccino.
# Coin Operated in course / Note Operated here.
# Notes accepted - 10, 20, 50, 100
# report input prints all resources left and money earned.
# commands available - exit, report, espresso, latte, cappuccino, admin
# exit command -> the program will close and all data will be reset.
# report command -> print report of how much water, milk, coffee available inside machine. Also how much money have earned.
# espresso, latte, cappuccino command -> will ask user to add quantity and then show the total price.
# after showing total price, the machine will show all the notes values we accept.
# users will enter how much 10, 20, 50 or 100 notes they want to enter in the machine.
# the machine will calculate amount received and total cost, then decide to proceed.
# give users return amount if they pay over price.
# refund whole amount if they pay less.
# my own addition, not available in course -> admin command, asking quantity, resources prices
# admin command -> it will ask for password, after entering correct password the admin can add water, milk or coffee to the machine.
# asking quantity -> when user enter, lets say, latte, than the machine will ask for quantity. This is not available in course. I added this feature for learning purpose.
# resources price -> while adding the resources inside the machine, the shopkeeper has to pay a price to buy those resources like water coffee and milk.
# here everything operates from the same display board, the shopkeeper / admin only knows those extra commands called admin, report and exit. the users only see choose from espresso, latte and cappuccino.
# liquid ingredients have units in ml, coffee has units in gram. prices are calculated in INR.
# Admin only thing -> the prices of ingredients are only for admin, milk and water are in ml, whereas coffee is in gram. price is based on INR.

machine_logo = '''
▗▄▄▄▖▗▖ ▗▖▗▄▄▄▖     ▗▄▄▖ ▗▄▖ ▗▄▄▄▖▗▄▄▄▖▗▄▄▄▖▗▄▄▄▖    ▗▖  ▗▖ ▗▄▖  ▗▄▄▖▗▖ ▗▖▗▄▄▄▖▗▖  ▗▖▗▄▄▄▖
  █  ▐▌ ▐▌▐▌       ▐▌   ▐▌ ▐▌▐▌   ▐▌   ▐▌   ▐▌       ▐▛▚▞▜▌▐▌ ▐▌▐▌   ▐▌ ▐▌  █  ▐▛▚▖▐▌▐▌   
  █  ▐▛▀▜▌▐▛▀▀▘    ▐▌   ▐▌ ▐▌▐▛▀▀▘▐▛▀▀▘▐▛▀▀▘▐▛▀▀▘    ▐▌  ▐▌▐▛▀▜▌▐▌   ▐▛▀▜▌  █  ▐▌ ▝▜▌▐▛▀▀▘
  █  ▐▌ ▐▌▐▙▄▄▖    ▝▚▄▄▖▝▚▄▞▘▐▌   ▐▌   ▐▙▄▄▖▐▙▄▄▖    ▐▌  ▐▌▐▌ ▐▌▝▚▄▄▖▐▌ ▐▌▗▄█▄▖▐▌  ▐▌▐▙▄▄▖
'''

admin_logo = '''
 ▗▄▖ ▗▄▄▄  ▗▖  ▗▖▗▄▄▄▖▗▖  ▗▖    ▗▄▄▖  ▗▄▖ ▗▖  ▗▖▗▄▄▄▖▗▖   
▐▌ ▐▌▐▌  █ ▐▛▚▞▜▌  █  ▐▛▚▖▐▌    ▐▌ ▐▌▐▌ ▐▌▐▛▚▖▐▌▐▌   ▐▌   
▐▛▀▜▌▐▌  █ ▐▌  ▐▌  █  ▐▌ ▝▜▌    ▐▛▀▘ ▐▛▀▜▌▐▌ ▝▜▌▐▛▀▀▘▐▌   
▐▌ ▐▌▐▙▄▄▀ ▐▌  ▐▌▗▄█▄▖▐▌  ▐▌    ▐▌   ▐▌ ▐▌▐▌  ▐▌▐▙▄▄▖▐▙▄▄▖
'''

drinks = {
    "espresso":{
        "ingredients":{
            "water":50,
            "coffee":18,
            "milk":0
        },
        "price":90,
    },
    "latte":{
        "ingredients":{
            "water":200,
            "coffee":24,
            "milk":150,
        },
        "price":180,
    },
    "cappuccino":{
        "ingredients":{
            "water":250,
            "coffee":24,
            "milk":100,
        },
        "price":280,
    },
}
machine_storage = {
    "water":1500,
    "coffee":300,
    "milk":900,
}
ingredients_purchase_cost = {
    "water":{
        "price":32,
        "quantity":100,
    },
    "coffee":{
        "price":55,
        "quantity":100,
    },
    "milk":{
        "price":72,
        "quantity":100,
    },
}
notes_accepted = [10, 20, 50, 100]

def display_board():
    print(machine_logo)
    print("What would you like? (espresso / latte / cappuccino)")

def the_user_input():
    the_command = input(": ").lower()
    if the_command == "exit":
        return False, the_command
    else:
        return True, the_command

def espresso(copy):
    drink_name = "espresso"
    the_purchase(copy, drink_name)

def latte(copy):
    drink_name = "latte"
    the_purchase(copy, drink_name)

def cappuccino(copy):
    drink_name = "cappuccino"
    the_purchase(copy, drink_name)

def report(copy):
    storage_now = copy["storage"]
    print(f'''We have
{storage_now["water"]} ml Water,
{storage_now["milk"]} ml Milk and
{storage_now["coffee"]} gm Coffee left.
Cash Earned till now is Rs:- {copy["cash"]} INR
''')

def admin(copy):
    the_password = copy["admin_password"]
    try:
        entered_pass = int(input("Enter Password: "))
        if entered_pass == the_password:
            admin_panel(copy)
        else:
            print("Wrong Password.")
    except ValueError:
        invalid_input()

#?  ================================ CALCULATIONS ================================

def machine_storage_calculator(details, name_of_drink, how_many_drinks):
    drink_water = resource_needed_after_user_input(details, name_of_drink, "water", how_many_drinks)
    drink_coffee = resource_needed_after_user_input(details, name_of_drink, "coffee", how_many_drinks)
    drink_milk = resource_needed_after_user_input(details, name_of_drink, "milk", how_many_drinks)
    details["storage"]["water"] -= drink_water
    details["storage"]["coffee"] -= drink_coffee
    details["storage"]["milk"] -= drink_milk

def received_from_user(data):
    print("We only accept", *data["notes"], "INR Notes.", sep=" ")
    received_value = 0
    try:
        for index in range(len(data["notes"])):
            note_how_many = abs(int(input(f"How many {data["notes"][index]} rupees notes you want to give?\n")))
            received_value += note_how_many * data["notes"][index]
        return received_value
    except ValueError:
        invalid_input()
        return 0

def total_cost_calculator(main_data, no_of_drink, name_of_drink):
    total_cost = main_data["drinks"][name_of_drink]["price"] * no_of_drink
    print(f"Here is your total cost: {total_cost} INR.")
    return total_cost

#?  ================================ HELPERS ================================

def the_purchase(the_data, name_of_the_drink):
    number_of_drinks = drink_quantity(name_of_the_drink)
    if number_of_drinks != 0:
        if storage_checker(the_data, number_of_drinks, name_of_the_drink):
            the_cost = total_cost_calculator(the_data, number_of_drinks, name_of_the_drink)
            user_input_amount = received_from_user(the_data)
            if user_input_amount >= the_cost:
                the_data["cash"] += the_cost
                machine_storage_calculator(the_data, name_of_the_drink, number_of_drinks)
                print('''=== PURCHASE SUCCESSFUL ===
Here is Your Drink''')
                if user_input_amount > the_cost:
                    take_refund(user_input_amount, the_cost)
            elif user_input_amount > 0:
                print(f"Sorry You paid less amount. Can't proceed. Here is your full refund: {user_input_amount} INR.")
            else:
                invalid_input()
        else:
            print("Sorry The Coffee Machine doesn't have enough resources.")
    else:
        invalid_input()

def invalid_input():
    print("That's an Invalid Input")

def admin_panel_logout_text():
    print("Logged Out from Admin Panel.")

def drink_quantity(name_of_drink):
    try:
        quantity = abs(int(input(f"How many {name_of_drink.title()} do you want? (eg: 1, 2, 3 etc etc)\n")))
        return quantity
    except ValueError:
        invalid_input()
        return 0

def storage_checker(details, how_many_drinks, name_of_drink):
    drink_water = resource_needed_after_user_input(details, name_of_drink, "water", how_many_drinks)
    drink_coffee = resource_needed_after_user_input(details, name_of_drink, "coffee", how_many_drinks)
    drink_milk = resource_needed_after_user_input(details, name_of_drink, "milk", how_many_drinks)
    if drink_water <= details["storage"]["water"] and drink_coffee <= details["storage"]["coffee"] and drink_milk <= details["storage"]["milk"]:
        return True
    else:
        return False

def resource_needed_after_user_input(full_data, drink_name, ingredient_name, how_many):
    total_resource = full_data["drinks"][drink_name]["ingredients"][ingredient_name] * how_many
    return total_resource

def resource_cost_finder(space_left, details, name_of_resource):
    return round((space_left / details["purchase_cost"][name_of_resource]["quantity"]) * details["purchase_cost"][name_of_resource]["price"])

def take_refund(user_paid, actual_cost):
    print(f"Take your refund. Rs:- {user_paid - actual_cost} INR")

def pay_and_add_ingredients(the_final_payable_cost, details):
    try:
        admin_pay = int(input(f"Pay Rs: {the_final_payable_cost}/-\n"))
        if admin_pay >= the_final_payable_cost:
            print("Ingredients added to coffee machine.")
            if admin_pay > the_final_payable_cost:
                take_refund(admin_pay, the_final_payable_cost)
            machine_filled_up(details)
            return False
        else:
            print(f"You paid only Rs: {admin_pay}/- which is less than Rs: {the_final_payable_cost}/-. Can't add ingredients to the machine.")
            return True
    except ValueError:
        invalid_input()
        return True

def machine_filled_up(data):
    data["storage"] = machine_storage.copy()
    print(f"Machine Filled Up. New storage: {data["storage"]} and Cash remains: {data["cash"]}")

#?  ================================ ADMIN PANEL ================================

def admin_panel(the_data):
    print("Welcome to admin panel.")
    while True:
        print(admin_logo)
        report(the_data)
        space_left_for_water = 1500 - the_data["storage"]["water"]
        space_left_for_coffee = 300 - the_data["storage"]["coffee"]
        space_left_for_milk = 900 - the_data["storage"]["milk"]
        cost_to_add_new_water = resource_cost_finder(space_left_for_water, the_data, "water")
        cost_to_add_new_coffee = resource_cost_finder(space_left_for_coffee, the_data, "coffee")
        cost_to_add_new_milk = resource_cost_finder(space_left_for_milk, the_data, "milk")
        total_cost = cost_to_add_new_water + cost_to_add_new_coffee + cost_to_add_new_milk
        cash_from_cashbox = the_data["cash"]
        user_consent = input(f"Cost of adding new ingredients is Rs: {total_cost} INR. Would you like to proceed? Y / N\n").lower()
        if user_consent == "y":
            add_cash_from_cashbox = input(f"You have Rs: {cash_from_cashbox} INR in your Cash Box from previous purchases. Would you like to add this amount? Y / N\n").lower()
            if add_cash_from_cashbox == "y":
                if cash_from_cashbox >= total_cost:
                    cash_remains_in_box = cash_from_cashbox - total_cost
                    the_data["storage"] = machine_storage.copy()
                    the_data["cash"] = cash_remains_in_box
                    machine_filled_up(the_data)
                    admin_panel_logout_text()
                    break
                else:
                    new_payable_amount = total_cost - cash_from_cashbox
                    if not pay_and_add_ingredients(new_payable_amount, the_data):
                        the_data["cash"] = 0
                        break
                    else:
                        continue
            elif add_cash_from_cashbox == "n":
                if not pay_and_add_ingredients(total_cost, the_data):
                    break
                else:
                    continue
            else:
                invalid_input()
        elif user_consent == "exit":
            admin_panel_logout_text()
            break
        else:
            continue

#!  ================================ MAPPER & MAIN ================================

def command_mapper(the_command, all_copies):
    saved_functions = {
        "espresso": espresso,
        "latte": latte,
        "cappuccino": cappuccino,
        "report": report,
        "admin": admin,
    }
    if the_command in saved_functions:
        saved_functions[the_command](all_copies)
    else:
        invalid_input()

def main():
    admin_password = 1234
    drinks_copy = drinks.copy()
    machine_storage_copy = machine_storage.copy()
    notes_accepted_copy = notes_accepted.copy()
    cash_box = 0
    purchase_cost = ingredients_purchase_cost.copy()
    all_copy_dict = {
        "drinks": drinks_copy,
        "storage": machine_storage_copy,
        "notes": notes_accepted_copy,
        "cash": cash_box,
        "admin_password": admin_password,
        "purchase_cost": purchase_cost,
    }
    while True:
        display_board()
        machine_running, user_input = the_user_input()
        if not machine_running:
            print("Thanks for using coffee machine. Have a productive day.")
            break
        else:
            command_mapper(user_input, all_copy_dict)

main()
