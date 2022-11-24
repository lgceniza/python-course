from turtle import *
import random

COLORS = [(202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41),
          (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149),
          (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171),
          (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), 
          (107, 127, 153), (176, 192, 208), (168, 99, 102)]

picasso = Turtle()
screen = Screen()

colormode(255)
screen.screensize(400, 200)

start_x = -200
start_y = -280
picasso.speed('fastest')
picasso.penup()
picasso.hideturtle()
picasso.goto(x=start_x, y=start_y)

for dot_count in range(100):
  if dot_count % 10 == 0:
    start_y += 50
    picasso.goto(x=start_x, y=start_y)

  picasso.dot(20, random.choice(COLORS))
  picasso.forward(40)

screen.exitonclick()