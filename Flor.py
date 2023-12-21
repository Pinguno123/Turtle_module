import turtle

# Configuración inicial
turtle.speed(15)
turtle.pensize(3)
turtle.bgcolor('black')

# Función para dibujar un pétalo
def draw_petal():
    turtle.circle(60, 70)
    turtle.left(120)
    turtle.circle(60, 70)
    turtle.left(120)

# Función para dibujar un tallo
def draw_stem():
    turtle.color('green')
    turtle.pensize(5)
    turtle.right(90)
    turtle.forward(200)
    turtle.left(90)

# Centrar el dibujo
turtle.penup()
turtle.goto(0, 0)
turtle.pendown()

# Dibujar las flores
turtle.color('white')
for _ in range(20):
    draw_petal()
    turtle.left(36)

turtle.penup()

# Dibujar el tallo
draw_stem()

turtle.hideturtle()
turtle.done()
