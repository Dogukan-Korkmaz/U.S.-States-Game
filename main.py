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

while game_is_on:
    answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?")
    if answer_state is None:
        screen.bye()
    for x in states:
        if x == answer_state.capitalize():
            print("bum")

turtle.mainloop()
