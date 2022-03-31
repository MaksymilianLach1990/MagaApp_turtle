import turtle
import logging

logging.basicConfig(level=logging.INFO)


# x szerokość
# y wysokośc
xWindow = 500
yWindow = 800

window = turtle.Screen()
window.title("MagaApp")
window.bgcolor("black")
window.setup(xWindow, yWindow, startx=0, starty=0)
window.tracer()


cursor = turtle.Turtle()
cursor.speed(0)
cursor.shape("triangle")
cursor.color("white")
cursor.penup()
cursor.goto(-250, 380)

pen = turtle.Turtle()
pen.speed()
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(-250, 380)

def generalMenu():
    pen.goto()

def moveCursorUp():
    logging.info(f"Cursor Y = {cursor.ycor()}")
    y = cursor.ycor()
    if y >= 380:
        return
    y += 20
    logging.info(f"Cursor Y = {cursor.ycor()}")
    cursor.sety(y)

def moveCursorDown():
    logging.info(f"Cursor Y = {cursor.ycor()}")
    y = cursor.ycor()
    if y <= -380:
        return
    y -= 20
    logging.info(f"Cursor Y = {cursor.ycor()}")
    cursor.sety(y)

# Keyboard binding
window.listen()
window.onkeypress(moveCursorUp, "Up")
window.onkeypress(moveCursorDown, "Down")


while True:
    window.update()


