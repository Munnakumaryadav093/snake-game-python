import turtle
import random
import time

delay = 0.1
score = 0
high_score = 0
bodies = []

# Screen
s1 = turtle.Screen()
s1.title("Snake Game")
s1.bgcolor("light blue")
s1.setup(width=600, height=600)

# Snake head
h1 = turtle.Turtle()
h1.shape("circle")
h1.speed(0)
h1.color("red")
h1.fillcolor("green")
h1.penup()
h1.goto(0, 0)
h1.direction = "stop"

# Food
f1 = turtle.Turtle()
f1.shape("square")
f1.speed(0)
f1.color("red")
f1.fillcolor("blue")
f1.penup()
f1.goto(200, 200)

# Scoreboard
sb = turtle.Turtle()
sb.ht()
sb.penup()
sb.goto(-250, 250)
sb.write("Score: 0 | High Score: 0", font=("Arial", 14, "normal"))

# Movement functions
def moveup():
    if h1.direction != "down":
        h1.direction = "up"

def movedown():
    if h1.direction != "up":
        h1.direction = "down"

def moveleft():
    if h1.direction != "right":
        h1.direction = "left"

def moveright():
    if h1.direction != "left":
        h1.direction = "right"

def movestop():
    h1.direction = "stop"

def move():
    if h1.direction == "up":
        h1.sety(h1.ycor() + 20)
    if h1.direction == "down":
        h1.sety(h1.ycor() - 20)
    if h1.direction == "left":
        h1.setx(h1.xcor() - 20)
    if h1.direction == "right":
        h1.setx(h1.xcor() + 20)

# Event Handling
s1.listen()
s1.onkey(moveup, "Up")
s1.onkey(movedown, "Down")
s1.onkey(moveright, "Right")
s1.onkey(moveleft, "Left")
s1.onkey(movestop, "space")

# MAIN GAME LOOP
while True:
    s1.update()

    # Border collision
    if h1.xcor() > 290 or h1.xcor() < -290 or h1.ycor() > 290 or h1.ycor() < -290:
        time.sleep(1)
        h1.goto(0, 0)
        h1.direction = "stop"

        # Hide bodies
        for b in bodies:
            b.ht()
        bodies.clear()

        score = 0
        sb.clear()
        sb.write(f"Score: {score} | High Score: {high_score}", font=("Arial", 14, "normal"))
        delay = 0.1

    # Food collision
    if h1.distance(f1) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        f1.goto(x, y)

        # Add body segment
        b1 = turtle.Turtle()
        b1.speed(0)
        b1.penup()
        b1.shape("square")
        b1.color("yellow")
        bodies.append(b1)

        score += 10
        if score > high_score:
            high_score = score

        sb.clear()
        sb.write(f"Score: {score} | High Score: {high_score}", font=("Arial", 14, "normal"))

        delay -= 0.001

    # Move snake body
    for i in range(len(bodies)-1, 0, -1):
        bodies[i].goto(bodies[i-1].xcor(), bodies[i-1].ycor())

    if len(bodies) > 0:
        bodies[0].goto(h1.xcor(), h1.ycor())

    move()

    # Self-collision
    for b in bodies:
        if b.distance(h1) < 20:
            time.sleep(1)
            h1.goto(0, 0)
            h1.direction = "stop"

            for b in bodies:
                b.ht()
            bodies.clear()

            score = 0
            sb.clear()
            sb.write(f"Score: {score} | High Score: {high_score}", font=("Arial", 14, "normal"))
            delay = 0.1

    time.sleep(delay)

s1.mainloop()
