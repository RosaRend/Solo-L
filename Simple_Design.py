import turtle

my_turtle = turtle.Turtle()

def square(lenght, angle):
  my_turtle.forward(length)
  my_turtle.left(angle)
  my_turtle.forward(length)
  my_turtle.left(angle)
  my_turtle.forward(length)
  my_turtle.left(angle)
  my_turtle.forward(length)
  
while 1 == 1:
  angle = 90
  angle = angle + 10
  
square(100, angle)  
