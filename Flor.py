import turtle

# Configuración inicial
turtle.pensize(3)
turtle.bgcolor('black')
turtle.Screen().setup(width=1.0, height=1.0)

# Función para dibujar un tallo y hoja
def draw_stem_and_leave(t):
    t.pensize(2)
    t.speed(1)
    t.setheading(88)    
    t.forward(250)

    # Dibujar hoja
    t.color('green')
    t.circle(80, 70)
    t.left(110)
    t.circle(80, 70)

# Función para dibujar un pétalo
def draw_petal(t):
    t.speed(15)
    t.circle(120, 70)
    t.left(120)
    t.circle(120, 70)
    t.left(120)

# Crear una copia de la tortuga principal
t1 = turtle.Turtle()
t1.color('white')

# Mover la copia a una posición diferente
t1.penup()
t1.goto(-200, 0)
t1.pendown()

# Ejecución del dibujo con ambas tortugas
for _ in range(10):
    draw_petal(turtle)
    draw_petal(t1)
    turtle.left(36)

# Mover ambas tortugas a la posición para el tallo y la hoja
turtle.penup()
turtle.goto(0, 0)
turtle.pendown()

t1.penup()
t1.goto(-200, 0)
t1.pendown()

# Dibujar el tallo y la hoja con ambas tortugas al mismo tiempo
draw_stem_and_leave(turtle)
draw_stem_and_leave(t1)

# Configuración de la ventana emergente
turtle.hideturtle()
t1.hideturtle()
turtle.done()
