# from turtle import Turtle
# import pandas
#
# data = pandas.read_csv("50_states.csv")
#
#
# class State(Turtle):
#
#     def __init__(self):
#         super().__init__()
#         self.penup()
#         self.hideturtle()
#
#     def go_string(self, state):
#         for s in data:
#             if state == s:
#                 s = data[data.state == state]
#                 rowx = s[1]
#                 rowy = s[2]
#                 self.goto(rowx, rowy)
#                 print(rowx, rowy)
