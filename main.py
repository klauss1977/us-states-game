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
game_on = True
while game_on:
    answer_state = screen.textinput(title=f"{correct_answers}/50 States Correct",
                                    prompt="What's another state name? ").title()
    print(answer_state)
    if answer_state:
        if answer_state in states_list:
            correct_answers += 1
            state_x = data[data.state == answer_state].x.values[0]
            state_y = data[data.state == answer_state].y.values[0]
            guessed_state.goto(state_x, state_y)
            guessed_state.write(f"{answer_state}")
    else:
        game_on = False

screen.exitonclick()
