print("============================")
print("WELCOME TO TREASURE ISLAND")
print("============================\n")

print("Your mission is to find the Treasure.\n")

print("You are at a cross road. Where do you want to go?")
direction = input("Type 'left' or 'right'\n")

if direction == "left" or direction == "Left":
    print("Great. There is an island in the middle of the lake. You want to 'wait' or 'swim'?")
    stop_go = input("Type 'wait or 'swim'\n")
    if stop_go == "wait" or stop_go == "Wait":
        print("Now there are 3 doors in front of you. The RED one | The BLUE one | The YELLOW one")
        choose_door = input("Choose one door. Type 'red', 'blue' or 'yellow'\n")
        if choose_door == "red" or choose_door == "Red" or choose_door == "blue" or choose_door == "Blue":
            print("Game Over")
        else:
            print("YEAH YOU WON!!!")
    else:
        print("Game Over")
else:
    print("Game Over")