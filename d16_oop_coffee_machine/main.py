from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

def main():
    drinks_menu = Menu()
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()
    while True:
        user_choice = input(f"What would you like? ({drinks_menu.get_items()}): ")
        if user_choice == "exit":
            print("Thanks for using Coffee Machine.")
            break
        elif user_choice == "report":
            coffee_maker.report()
            money_machine.report()
        else:
            the_drink = drinks_menu.find_drink(user_choice)
            if the_drink:
                if coffee_maker.is_resource_sufficient(the_drink):
                    if money_machine.make_payment(the_drink.cost):
                        coffee_maker.make_coffee(the_drink)

main()
