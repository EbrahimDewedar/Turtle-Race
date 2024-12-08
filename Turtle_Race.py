import random
from turtle import Turtle, Screen
monitor = Screen()
monitor.setup(width = 500, height = 400)
user_bet = monitor.textinput(title = "the turtle game", prompt = "which turtle will win the game ? choose a color:")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_pos = [-80, -50, -20, 10, 40, 70]
is_race_on = False
all_turtles = []
for turtle_index in range(6):
    tim = Turtle(shape = "turtle")
    tim.color(colors[turtle_index])
    tim.penup()
    tim.goto(x = -230, y = y_pos[turtle_index])
    all_turtles.append(tim)
if user_bet:
    is_race_on = True
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winner_color = turtle.pencolor()
            if user_bet == winner_color:
                print(f"you've won the {winner_color} turtle is the winner")
            else:
                print(f"you've lost the {winner_color} turtle is the winner")
        turtle.forward(random.randint(1,10))

monitor.exitonclick()




