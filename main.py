import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states_list = data.state.to_list()
state_turtle = turtle.Turtle()
state_turtle.penup()
state_turtle.hideturtle()
guessed_states_list = []
while len(guessed_states_list) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states_list)}/50 States Correct",
                                    prompt="What's another state name? ").title()
    if answer_state == "Exit":
        states_to_learn = [state for state in states_list if state not in guessed_states_list]
        pandas.DataFrame(states_to_learn).to_csv("states_to_learn.csv")
        break
    if answer_state in states_list:
        guessed_states_list.append(answer_state)
        state_x = data[data.state == answer_state].x.values[0]
        state_y = data[data.state == answer_state].y.values[0]
        state_turtle.goto(state_x, state_y)
        state_turtle.write(f"{answer_state}")



