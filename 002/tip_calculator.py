print("=== === === === ===")
print("This is a TIP CALCULATOR")
print("=== === === === ===")

# What was the total bill?

total_bill = input("What is the total bill?\n")

# How much percent tip would yiu like to give?

tip_percent = input("How much percent tip is applied?\n")

# How many people to split the bill?

total_people = input("How many people should split the bill?\n")

# Check the data from input

print(f"Here total bill is {total_bill}, tip percentage is {tip_percent} and there are {total_people} people available")

# Develop the logic behind it.

the_tip = round((total_bill * 100 / tip_percent), 2)
final_tip = total_bill + the_tip

# Each person should pay: Result

each_pay = round((final_tip / total_people), 2)

print(f"Each person should pay {each_pay}")

