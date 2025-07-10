import random
from turtle import Turtle, Screen

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = None
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [120, 70, 20, -20, -70, -120]
all_turtles = []

def create_turtle(color, y):
    new_turtle = Turtle("turtle")
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y)
    return new_turtle

for index in range(len(colors)):
    new_turtle1 = create_turtle(colors[index], y_positions[index])
    all_turtles.append(new_turtle1)

while user_bet not in colors:
    user_bet = screen.textinput(
        title="Make your bet",
        prompt=f"Which turtle will win the race? Enter a color\n{', '.join(colors)}: ").lower()
    if user_bet:
        user_bet = user_bet.lower()
    else:
        break
        
if user_bet in colors:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner! 🐢")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
