import turtle

# Configuración inicial
turtle.speed(15)
turtle.pensize(3)
turtle.bgcolor('black')

def draw_petal():
    turtle.circle(120, 70)  # Aumenté el radio del círculo
    turtle.left(120)
    turtle.circle(120, 70)
    turtle.left(120)

# Centrar el dibujo
turtle.penup()
turtle.goto(0, 0)
turtle.pendown()

turtle.color('white')
for _ in range(20):
    draw_petal()
    turtle.left(36)

def draw_stem():
    turtle.color('red')
    turtle.goto(0, -20)
    turtle.forward(100)



turtle.hideturtle()
turtle.done()
