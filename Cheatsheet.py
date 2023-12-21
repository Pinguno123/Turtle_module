import turtle

# Configuración inicial
turtle.speed(2)      # Configura la velocidad de la tortuga (1: más lento, 10: más rápido)
turtle.pensize(2)    # Configura el grosor de la pluma
turtle.bgcolor("white")  # Configura el color de fondo

# Movimientos básicos
turtle.forward(100)  # Avanzar 100 unidades
turtle.backward(50)  # Retroceder 50 unidades
turtle.right(90)     # Girar 90 grados a la derecha
turtle.left(45)      # Girar 45 grados a la izquierda

# Pluma
turtle.penup()       # Levanta la pluma (no dibuja)
turtle.pendown()     # Baja la pluma (dibuja)

# Cambiar colores
turtle.color("red")  # Configura el color de la pluma
turtle.fillcolor("blue")  # Configura el color de relleno

# Dibujar formas
turtle.circle(50)    # Dibuja un círculo con radio 50
turtle.square(80)    # Dibuja un cuadrado con lado 80

# Control de la ventana
turtle.hideturtle()  # Oculta la tortuga
turtle.showturtle()  # Muestra la tortuga
turtle.done()        # Cierra la ventana al hacer clic