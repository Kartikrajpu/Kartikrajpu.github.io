import turtle

# Create a turtle object
t = turtle.Turtle()

# Set the turtle's pen color to gray
t.color("gray")

# Move the turtle to the starting position for the elephant's head
t.penup()
t.goto(-100, 0)
t.pendown()

# Draw the elephant's head
t.begin_fill()
t.circle(50)
t.end_fill()

# Draw the elephant's trunk
t.left(90)
t.forward(100)
t.right(90)
t.forward(25)
t.left(90)
t.forward(50)

# Draw the elephant's ears
t.penup()
t.goto(-75, 50)
t.pendown()
t.left(30)
t.forward(50)
t.right(60)
t.forward(50)

t.penup()
t.goto(-125, 50)
t.pendown()
t.right(30)
t.forward(50)
t.left(60)
t.forward(50)

# Draw the elephant's eyes
t.penup()
t.goto(-65, 75)
t.pendown()
t.dot(10)
t.penup()
t.goto(-135, 75)
t.pendown()
t.dot(10)

# Hide the turtle
t.hideturtle()

# Keep the turtle window open until the user closes it
turtle.mainloop()
