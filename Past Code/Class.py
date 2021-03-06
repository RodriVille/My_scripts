#   a114_guess.py
import turtle as trtl

painter = trtl.Turtle()
painter.speed(0)
painter.penup()
painter.color("salmon")
painter.pensize(2)

spiral_space = int(0)

while (spiral_space < 80): 
  painter.goto(0,0)
  painter.right(26-spiral_space/4)
  painter.forward(42+(spiral_space*1.5))
  painter.pendown()
  painter.circle(10)
  painter.penup()
  spiral_space = spiral_space + 1
  if (spiral_space % 5 == 0):
    painter.color("navy")
  if (spiral_space % 10 == 0):
    painter.color("salmon")

wn = trtl.Screen()
wn.mainloop()