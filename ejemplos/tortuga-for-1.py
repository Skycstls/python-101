from turtle import *

value1=1
angle=90

#make it faster
speed(0)

for i in range(400):
    forward(value1)
    left(angle)
    value1+=1

exitonclick()