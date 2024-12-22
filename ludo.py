# from turtle import*
# bgcolor("white")
# color("Black","brown")
# begin_fill()
# left(90)
# forward(60)
# circle(25,95)
# forward(100)
# circle(10,200)
# right(45)
# forward(12)
# right(90)
# forward(300)
# right(60)
# circle(50,200)
# right(80)
# circle(55,200)
# right(80)
# forward(250)
# right(85)
# circle(20,85)
# end_fill()
# done()




from turtle import Turtle, Screen

# Setup screen
screen = Screen()
screen.bgcolor("white")

# Create turtle instance
t = Turtle()
t.color("Black", "brown")
t.speed(1)

# Start drawing and filling
t.begin_fill()

t.left(90)
t.forward(60)
t.circle(25, 95)
t.forward(100)
t.circle(10, 200)
t.right(45)
t.forward(12)
t.right(90)
t.forward(300)
t.right(60)
t.circle(50, 200)
t.right(80)
t.circle(55, 200)
t.right(80)
t.forward(250)
t.right(85)
t.circle(20, 85)

# End fill and finish
t.end_fill()
t.hideturtle()
screen.mainloop()
