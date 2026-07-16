from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

drinks_menu = Menu()                    #! menu / get_items() / find_drink(order_name)
coffee_maker = CoffeeMaker()            #! report() / is_resource_sufficient(drink) / make_coffee(order)
money_machine = MoneyMachine()          #! report() / process_coins() / make_payment(cost)

def main():
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
