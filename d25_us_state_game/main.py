
import turtle
import pandas

screen = turtle.Screen()
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
correct_guesses = []
remaining_states = []
state_data = pandas.read_csv("50_states.csv")
all_state_list = state_data.state.to_list()
game_running = True
while game_running:
    user_input = screen.textinput(title="State Name Guessing Game", prompt=f"{len(correct_guesses)}/50 Correct Guess").title()
    if user_input == "Exit":
        break
    if user_input in all_state_list and user_input not in correct_guesses:
        correct_guesses.append(user_input)
        state_name_turtle = turtle.Turtle()
        state_name_turtle.shape("square")
        state_name_turtle.hideturtle()
        state_name_turtle.penup()
        state_name_turtle.goto(state_data.x[state_data.state == user_input].to_list()[0], state_data.y[state_data.state == user_input].to_list()[0])
        state_name_turtle.write(user_input, align="center", font=("Arial", 12, "normal"))
        if len(correct_guesses) == 50:
            game_running = False

for state_name in all_state_list:
    if state_name not in correct_guesses:
        remaining_states.append(state_name)

pandas.DataFrame({"states":remaining_states}).to_csv("another_remaining_states.csv")