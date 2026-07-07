def first_user_input():
    first_number = int(input("What's the first number?\n"))
    return first_number

def second_user_input():
    operation_chooser = str(input('''
+
-
*
/
Pick an operation: 
'''))
    second_number = int(input("What's the second number?\n"))
    return second_number, operation_chooser

def the_calculation(first_number, second_number, the_operator):
    if the_operator == "+":
        return first_number + second_number
    elif the_operator == "-":
        return first_number - second_number
    elif the_operator == "*":
        return first_number * second_number
    elif the_operator == "/":
        if second_number != 0:
            return round((first_number / second_number), 2)
        else:
            print("Division by 0 is not permitted")
    else:
        return None

def display_result(first_number, second_number, the_operator, result):
    print(first_number, the_operator, second_number, "=", result)

def new_calculation_or_not(result):
    user_consent = input(f"Type 'Y' to continue calculating with {result}, type 'N' to start afresh\n").lower()
    if user_consent == "y":
        return True, result
    else:
        print("\n" * 50)
        return False, None

def program_stopper():
    user_consent = input("Type 'Y' to start a new calculation, Type 'N' to stop the program.\n").lower()
    if user_consent == "y":
        return True
    else:
        print("Thanks for using the calculator")
        return False

def main():
    program_continues = True
    while program_continues:
        first_no = first_user_input()
        calculation_continues = True
        while calculation_continues:
            second_no, operator = second_user_input()
            the_result = the_calculation(first_no, second_no, operator)
            if the_result != None:
                display_result(first_no, second_no, operator, the_result)
                calculation_continues, first_no = new_calculation_or_not(the_result)
        program_continues = program_stopper()

main()
