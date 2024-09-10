import math
from turtle import *
def heart_1(a):
    return 15*math.sin(a)**3
def heart_2(a):
    return 12*math.cos(a)-5*\
         math.cos(2*a)-2*\
         math.cos(3*a)-\
         math.cos(4*a)
speed(100000000)
bgcolor("#8FD3FE")
for i in range(6000):
    goto(heart_1(i)*20,heart_2(i)*20)
    for j in range(5):
        color("white")
    goto(0,0)
done()        
