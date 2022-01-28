from turtle import Turtle, Screen
import random

screen = Screen()
# set the possible colors of the turtles
colors = ["red", "orange", "yellow", "blue", "purple", "cyan", "dark orange", "medium spring green", "dodger blue"]
# set the size of the screen.
screen.setup(width=1000, height=800)
is_race_on = False
# getting the bet from the user
user_bet = screen.textinput(title="Make your bet", prompt=f"Which turtle will win the race? \n{colors}")
all_turtels = []
# setting possible y coordinates
yCoordinates = [0, -80, -160, -240, -320, 80, 160, 240, 320]
# for loop that creates a turtle object with random color, turtle shape,setting its random y pos from the y list then
# remove this y from the list.
# same thing with the color (so each turtle will be with different color and at different pos).
# pen up so it won't leave any trace
for index in range(len(colors)):
    new_turtle = Turtle(shape="turtle")
    color = (random.choice(colors))
    new_turtle.color(color)
    all_turtels.append(new_turtle)
    colors.remove(color)
    new_turtle.penup()
    ycor = random.choice(yCoordinates)
    new_turtle.goto(x=-470, y=ycor)
    yCoordinates.remove(new_turtle.ycor())
# if the bet we can start the race
if user_bet:
    is_race_on = True
# when the race is on we want to check if we got a winner if we do, end the race then print to the user the outcome.
# if we don't have a winner we want to let every turtle move forward random distance.
while is_race_on:
    for turtle in all_turtels:
        if turtle.xcor() >= 480:
            is_race_on = False
            winning_col = turtle.pencolor()
            if winning_col == user_bet:
                screen.title(f"You've won! The {winning_col} turtle is the winner")
            else:
                screen.title(f"You've lost! The {winning_col} turtle is the winner")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
