from turtle import *
from random import randint

# Generador de árbol aleatorio
def tree(branchLen, t):
    if branchLen > 5:
        t.forward(branchLen)
        t.right(20)
        tree(branchLen-15, t)
        t.left(40)
        tree(branchLen-15, t)
        t.right(20)
        t.backward(branchLen)

t = Turtle()
t.left(90)
t.up()
t.backward(100)
t.down()
tree(75, t)
exitonclick()