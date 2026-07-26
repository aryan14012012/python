import turtle 

# Setup screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Geometric Shapes by Aryan")

# Create turtle
board = turtle.Turtle()
board.speed("fastest")
board.hideturtle()

# ========== SHAPE 1: Colorful Spiral ==========
colors = ["red","green","blue","lime","yellow","cyan","violet","pink","white"]
for i in range(80):
    board.color(colors[i % len(colors)])
    board.width(2)
    board.forward(i * 2)
    board.right(91)

# ========== SHAPE 2: Golden Star ==========
board.penup() 
board.goto(0, -60) 
board.setheading(90)
board.pendown()
board.color("gold", "yellow")
board.begin_fill()
for i in range(5):
    board.forward(130) 
    board.right(144)
board.end_fill()

# ========== SHAPE 3: Square Pattern ==========
board.penup()
board.goto(0, 0)
board.pendown()
petal_colors = ["cyan","lime","violet","orange","deeppink"]
for i in range(36):
    board.color(petal_colors[i % len(petal_colors)],
                petal_colors[(1 + 2) % len(petal_colors)])
    board.begin_fill()
    for j in range(4):
        board.forward(55)
        board.right(90)
    board.end_fill()
    board.right(10)

# ========== SHAPE 4: Circle ==========
board.penup()
board.goto(-250, 200)
board.pendown()
board.setheading(0)
circle_colors = ["orange", "red"]
board.color(circle_colors[0], circle_colors[1])
board.begin_fill()
board.circle(50)
board.end_fill()

# ========== SHAPE 5: Triangle ==========
board.penup()
board.goto(250, 200)
board.pendown()
board.setheading(0)
board.color("magenta", "violet")
board.begin_fill()
for i in range(3):
    board.forward(100)
    board.left(120)
board.end_fill()

# ========== SHAPE 6: Hexagon ==========
board.penup()
board.goto(-250, -200)
board.pendown()
board.setheading(0)
board.color("cyan", "blue")
board.begin_fill()
for i in range(6):
    board.forward(60)
    board.left(60)
board.end_fill()

# ========== SHAPE 7: Pentagon ==========
board.penup()
board.goto(250, -200)
board.pendown()
board.setheading(0)
board.color("lime", "green")
board.begin_fill()
for i in range(5):
    board.forward(80)
    board.left(72)
board.end_fill()

# ========== SHAPE 8: Rectangle ==========
board.penup()
board.goto(0, -250)
board.pendown()
board.setheading(0)
board.color("yellow", "orange")
board.begin_fill()
for i in range(2):
    board.forward(120)
    board.left(90)
    board.forward(60)
    board.left(90)
board.end_fill()

# ========== SHAPE 9: Nested Squares ==========
board.penup()
board.goto(-150, 0)
board.pendown()
board.setheading(0)
nested_colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
for i in range(7):
    board.color(nested_colors[i])
    size = 100 - (i * 12)
    for j in range(4):
        board.forward(size)
        board.left(90)

# ========== SHAPE 10: Concentric Circles ==========
board.penup()
board.goto(150, 0)
board.pendown()
board.setheading(0)
concentric_colors = ["red", "orange", "yellow", "green", "blue", "purple"]
for i in range(6):
    board.color(concentric_colors[i])
    board.width(3)
    board.circle(10 + (i * 10))

turtle.done()