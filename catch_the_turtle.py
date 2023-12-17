import turtle
import time
import random

def increase_score(x, y):
    global score
    score += 1
    turtle_score.clear()
    turtle_score.write(f'Score: {score}', font=("Times New Roman", 22, "bold"))

def move_turtle():
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    turtle_turtle.goto(x, y)
    if time_counter > 0:
        turtle_screen.ontimer(move_turtle, 500)

def start_game():
    global time_counter
    while time_counter > 0:
        turtle_time.clear()
        turtle_time.write(f'Time: {time_counter}', font=("Times New Roman", 22, "bold"))
        time.sleep(0.5)
        time_counter -= 1

    turtle_time.clear()
    turtle_time.write('Game Over!', font=("Times New Roman", 22, "bold"))
    turtle_turtle.onclick(None)


turtle_screen = turtle.Screen()
turtle_screen.bgcolor("Light blue")
turtle_screen.title("Catch the Turtle")


score = 0
turtle_score = turtle.Turtle()
turtle_score.hideturtle()
turtle_score.penup()
turtle_score.color("blue")
turtle_score.goto(-50, 350)
turtle_score.write('Score: 0', font=("Times New Roman", 22, "bold"))


turtle_turtle = turtle.Turtle()
turtle_turtle.shape("turtle")
turtle_turtle.color("green")
turtle_turtle.shapesize(stretch_wid=1.5, stretch_len=1.5)
turtle_turtle.penup()
turtle_turtle.onclick(increase_score)


turtle_time = turtle.Turtle()
turtle_time.hideturtle()
turtle_time.penup()
turtle_time.color("black")
turtle_time.goto(-50, 300)
time_counter = 20


move_turtle()
start_game()

turtle_screen.mainloop()
