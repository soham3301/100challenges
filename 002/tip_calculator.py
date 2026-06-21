print("=== === === === ===")
print("This is a TIP CALCULATOR")
print("=== === === === ===")

# What was the total bill?
total_bill = round(float(input("What is the total bill?\n")), 2)

# How much percent tip would yiu like to give?
tip_percent = round(float(input("How much percent tip is applied?\n")), 2)

# How many people to split the bill?
total_people = round(float(input("How many people should split the bill?\n")))

# Check the data from input
print(f"Here total bill is {total_bill} doller, tip percentage is {tip_percent} and there are {total_people} people available")

# Develop the logic behind it.
# print(type(total_bill))
# print(type(total_people))
# print(type(tip_percent))

the_tip = round(float(total_bill * tip_percent / 100))
final_tip = round(float(total_bill + the_tip), 2)

# Each person should pay: Result

each_pay = round((final_tip / total_people), 2)

print(f"Each person should pay {each_pay}")

