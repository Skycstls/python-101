from turtle import *
from random import randint

tortugas = []

for i in range(200):
    tortugas.append(Turtle())

for tortuga in tortugas:
    tortuga.left(randint(0,360))
    tortuga.forward(randint(1,500))

exitonclick()
    