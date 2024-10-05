from turtle import *
from random import randint

tortugas = []

rango = range(0,360,1)

for i in rango:
    tortugas.append(Turtle())

for tortuga, index in zip(tortugas, rango):
    tortuga.speed(0)
    tortuga.left(index)
    tortuga.forward(500)
    tortuga.hideturtle()


exitonclick()
    