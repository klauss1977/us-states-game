import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states_list = data.state.to_list()
guessed_state = turtle.Turtle()
guessed_state.penup()
guessed_state.hideturtle()
correct_answers = 0
guessed_states_list = []
while len(guessed_states_list) < 50:
    answer_state = screen.textinput(title=f"{correct_answers}/50 States Correct",
                                    prompt="What's another state name? ").title()
    if answer_state == "Exit":
        break
    if answer_state in states_list:
        correct_answers += 1
        guessed_states_list.append(answer_state)
        state_x = data[data.state == answer_state].x.values[0]
        state_y = data[data.state == answer_state].y.values[0]
        guessed_state.goto(state_x, state_y)
        guessed_state.write(f"{answer_state}")


states_to_learn = {"State name":[]}
for state in states_list:
    if state not in guessed_states_list:
        states_to_learn["State name"].append(state)
print(states_to_learn)
pandas.DataFrame(states_to_learn).to_csv("states_to_learn.csv")
