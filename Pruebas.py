#Importación de la libreria Turtle
import turtle

# Configuración inicial
turtle.pensize(3)
turtle.bgcolor('black')

#Pantalla completa
turtle.Screen().setup(width=1.0, height=1.0)

#Partes del dibujo
def draw_stem():
    turtle.pensize(2)
    turtle.speed(1)
    turtle.setheading(88)    
    turtle.forward(250)

def draw_petal():
    turtle.speed(3)
    turtle.circle(120, 70)
    turtle.left(120)
    turtle.circle(120, 70)
    turtle.left(120)

def draw_leave():
    turtle.speed(1)
    turtle.circle(80, 70)
    turtle.left(110)
    turtle.circle(80, 70)

#Centrado del dibujo
turtle.penup()
turtle.goto(0, 0)
turtle.pendown()

#Ejecución del dibujo
turtle.color('white')
for _ in range(20):
    draw_petal()
    turtle.left(36)

turtle.penup()
turtle.goto(15, -250)
turtle.pendown()

draw_stem()

turtle.penup()
turtle.goto(15, -200)
turtle.pendown()

draw_leave()

#Configuración de la ventana emergente
turtle.hideturtle()
turtle.done()