from turtle import Turtle, Screen
import random
my_screen = Screen()
my_screen.setup(width=600, height=500)
my_screen.textinput("choice","which turtle would win?")
colors = ["orange","yellow","green","red","pink","purple","black"]
w = -290
h = -150
steps = [10, 20, 30, 15, 17]

for i in range(0,6):
    tim = Turtle(shape="turtle")
    tim.penup()
    tim.color(colors[i])
    tim.goto(w,h)
    h = h+40
    while w != 600:
        tim.forward(random.choice(steps))
my_screen.exitonclick()