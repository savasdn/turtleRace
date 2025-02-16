from random import randint
from turtle import Turtle, Screen

is_race_on = False
screen = Screen()
screen.setup(500,400)
user_bet = screen.textinput("Make your bet", "Which turtle will win the race. Choose your color: ")
color = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-120, -80, -40, 0, 40, 80]
all_turtle = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color[turtle_index])
    new_turtle.penup()
    new_turtle.speed(100)
    new_turtle.goto(x = -230, y = y_positions[turtle_index])
    all_turtle.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        turtle.forward(randint(1,10))
        if turtle.xcor() > 225:
            is_race_on = False
            if user_bet == turtle.pencolor():
                print(f"You win. The {turtle.pencolor()} is the winner.")
            else:
                print(f"You lose. the {turtle.pencolor()} is the winner.")


screen.exitonclick()