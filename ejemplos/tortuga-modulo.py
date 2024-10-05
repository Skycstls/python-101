from turtle import *
from random import randint, choice

directions = [0, 90, 180, 270]
speed(0)

#move a random amount then turn a random amount

for i in range(3000):
    forward(randint(1,3))
    left(choice(directions))

exitonclick()
