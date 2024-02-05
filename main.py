import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


data = pandas.read_csv("50_states.csv")
states = data["state"]
states.to_list()

game_is_on = True
score = 0

while game_is_on:
    answer_state = screen.textinput(title=f"Guess the State ({score}/50)", prompt="What's another state's name?")
    if answer_state is None:
        screen.bye()
    for state_answer in states:
        if state_answer == answer_state.capitalize():
            score += 1

turtle.mainloop()

