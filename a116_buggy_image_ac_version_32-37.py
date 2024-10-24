# a116_ladybug.py
import turtle as trtl
ladybug = trtl.Turtle()
ladybug.pensize(40)
ladybug.circle(5)
#head

ladybug.penup()
ladybug.goto(0, -55)
ladybug.color("red")
ladybug.pendown()
ladybug.pensize(40)
ladybug.circle(20)
ladybug.setheading(270)
ladybug.color("black")
ladybug.penup()
ladybug.goto(0, 5)
ladybug.pensize(2)
ladybug.pendown()
ladybug.forward(75)
#body

num_dots = 0
max_dots = 2
xpos = -20
ypos = -55
ladybug.pensize(10)
#config dots

while num_dots < max_dots:
  ladybug.penup()
  ladybug.goto(xpos, ypos)
  ladybug.pendown()
  ladybug.circle(3)
  ladybug.penup()
  ladybug.goto(xpos + 30, ypos + 20)
  ladybug.pendown()
  ladybug.circle(2)
  xpos += 10
  ypos += 25
  num_dots += 1  
  #pos next dots
#draw dots

ladybug.hideturtle()
wn = trtl.Screen()
wn.mainloop()
