# name:     TAMIRAT DEREJE
# Id:       UGR/5111/12
# section   3
import turtle
from turtle import *
hour = turtle.Turtle()
mint = turtle.Turtle()
sec = turtle.Turtle()
circle = turtle.Turtle()
getscreen().bgcolor('black')


# Defining the function that draw the center
def center():
    begin_fill()
    circle.color('brown')
    circle.up()
    circle.speed(0)
    circle.goto(9, -2)
    circle.down()
    circle.circle(radius=10)
    end_fill()
# Defining the function that draw the circle
def circle_drawer():
    begin_fill()
    circle.color('white')
    circle.up()
    circle.speed(0)
    circle.goto(0, 200)
    circle.setheading(180)
    circle.pensize(5)
    circle.down()
    circle.hideturtle()
    circle.circle(radius=200)
    circle.up()
    circle.goto(0, 0)
    end_fill()
# Defining the function that draw numbers inside the circle

def circle_num():
    circle.setheading(90)
    num_pointer_a = 0
    while num_pointer_a < 4:
        circle.up()
        circle.speed(0)
        circle.pensize(1)
        circle.forward(165)
        circle.color('white')
        circle.down()
        circle.write(12-3*num_pointer_a)
        circle.up()
        circle.goto(0, 0)
        circle.left(90)
        num_pointer_a += 1
    num_pointer_b = 0
    while num_pointer_b < 60:
        circle.up()
        circle.speed(0)
        circle.goto(0, 0)
        if num_pointer_b % 5 == 0:
            circle.color('red')
            circle.forward(173)
            circle.down()
            circle.forward(20)
        else:
            circle.color('white')
            circle.forward(180)
            circle.down()
            circle.forward(13)
        circle.up()
        circle.goto(0, 0)
        circle.right(6)
        num_pointer_b += 1
# Defining the function that draw second arm
def second():
    sec.color('gray')
    sec.pensize(2)
    sec.speed(0)
    sec.setheading(90)
    sec_counter = 0
    while sec_counter < 60:
        sec.clear()
        sec.hideturtle()
        sec.speed(0)
        sec.right(6)
        sec.forward(160)
        sec.up()
        sec.speed(1)
        sec.goto(0, 0)
        sec.down()
        sec_counter += 1
# Defining the function that draw minute arm
def minute():
    min_setter()
    mint.setheading(90)
    min_counter = 0
    while min_counter < 60:
        second()
        mint.clear()
        mint.hideturtle()
        mint.speed(0)
        mint.right(6)
        mint.forward(140)
        mint.up()
        mint.goto(0, 0)
        mint.down()
        min_counter += 1
# Defining the function that draw hour arm
def hour_hand():
    hour_setter()
    while True:
        minute()
        hour.speed()
        hour.clear()
        hour.down()
        hour.right(30)
        hour.forward(70)
        hour.up()
        hour.goto(0, 0)


# Defining the function that set hour arm before the clock start counting
def hour_setter():
    hour.setheading(0)
    hour.speed(0)
    hour.pensize(4)
    hour.hideturtle()
    hour.color('gray')
    hour.forward(70)
    hour.up()
    hour.goto(0, 0)
    hour.down()
# Defining the function that set minute arm before the clock start counting
def min_setter():
    mint.setheading(90)
    mint.pensize(4)
    mint.color('gray')
    mint.speed()
    mint.hideturtle()
    mint.forward(140)
    mint.up()
    mint.backward(140)
    mint.pendown()


circle_drawer()
circle_num()
center()
while True:
    hour_hand()