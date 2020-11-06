#   a113_flower.py
#   This code draws a flower.
import turtle as trtl

painter = trtl.Turtle()
painter.speed(0)

# stem
painter.color("green")
painter.pensize(15)
painter.goto(0, -150)
painter.setheading(90)
painter.forward(100)
#  leaf
painter.setheading(270)
painter.circle(20, 120, 20)
painter.setheading(90)
painter.goto(0, -60)
# rest of stem
painter.forward(60)
painter.setheading(0)
# change pen
painter.penup()
painter.shape("circle")
painter.turtlesize(2)

# draw flower
painter.goto(20,190)
petals = 0
while (petals < 18):
  painter.color("darkorchid")
  painter.right(20)
  painter.forward(30)
  rem = petals % 2
  rem2 = petals % 4
  if (rem == 0):
    painter.color("blue")
  if (rem2 == 0):
    painter.color("red")
  painter.stamp()
  petals = petals + 1
  
# ring 2 of flower
painter.goto(20,160)
petals = 0
while (petals < 12):
  painter.color("orange")
  painter.right(30)
  painter.forward(30)
  rem = petals % 2
  if (rem == 0):
    painter.color("black")
  painter.stamp()
  petals = petals + 1

# ring 3 of flower
painter.goto(20,130)
petals = 0
while (petals < 8):
    painter.color("pink")
    painter.right(45)
    painter.forward(20)
    rem = petals % 2
    if (rem == 0):
       painter.color("green")
    painter.stamp()
    petals = petals + 1
  
wn = trtl.Screen()
wn.mainloop()