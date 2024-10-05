from turtle import *

def move(val):
    forward(val)
    left(val)
    
def repeat(fun):
    for i in range(360):
        fun(1)

repeat(move)
