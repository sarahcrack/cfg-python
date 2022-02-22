from turtle import *

# house outline
for i in range(4):
    forward(200)
    left(90)

forward(120)
left(90)

# door
forward(100)
right(90)
forward(50)
right(90)
forward(100)

# getting into position for door handle
penup()
right(180)
forward(70)
left(90)
forward(10)

# door handle /  colour
pendown()
fillcolor("green")
begin_fill()
circle(3)
end_fill()

penup()
right(90)
forward(100)
left(90)
forward(140)
pendown()

# windows
for i in range(4):
    left(90)
    forward(60)
penup()

# window frame
left(90)
forward(30)
left(90)
pendown()
forward(60)
penup()
left(90)
forward(30)
left(90)
forward(30)
pendown()
left(90)
forward(60)
penup()

#position for roof
left(180)
forward(90)
left(90)
forward(50)
right(90)
pendown()

#roof
right(45)
forward(142)
right(90)
forward(142)
penup()

# sun position
left(45)
forward(40)
left(90)
forward(50)
pendown()

# pattern
pencolor("yellow")
for i in range(50):
    forward(60)
    left(123)


done()



