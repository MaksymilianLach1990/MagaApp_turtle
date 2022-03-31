import turtle
import logging

logging.basicConfig(level=logging.DEBUG)


# x szerokość
# y wysokośc

# Basic Variable
xWindow = 500
yWindow = 800
startPoint = (-230, 320)
items = ["Apple", "Orange", "Tant", "Dog", "Cat"]
page = "Ap"

# Window
window = turtle.Screen()
window.title("MagaApp")
window.bgcolor("black")
window.setup(xWindow, yWindow, startx=0, starty=0)
window.tracer()

# Cursor
cursor = turtle.Turtle()
cursor.speed(0)
cursor.shape("triangle")
cursor.color("white")
cursor.penup()
cursor.goto(-250, 340)

# Pen for the text
pen = turtle.Turtle()
pen.speed()
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(-240, 380)

# General Menu
def generalMenu():
    gMenu = ["Items", "Settings", "Containers", "Exit"]
    logging.debug("Print General Menu")
    # Print page title
    pen.penup()
    pen.goto(-50, (yWindow/2)-40)
    pen.write("Menu Główne", font=("Arial", 20, "bold"))

    # Print elements
    logging.debug("Print Elements from gMenu")
    pen.goto(startPoint)
    for element in gMenu:
        pen.write(element, font=("Ariel", 20, "bold"))
        y = pen.ycor()
        y -= 40
        pen.sety(y)


def moveCursorUp():
    logging.debug(f"Cursor from Y = {cursor.ycor()}")
    y = cursor.ycor()
    if y >= 340:
        return
    y += 40
    cursor.sety(y)
    logging.debug(f"Cursor to Y = {cursor.ycor()}")

def moveCursorDown():
    logging.debug(f"Cursor from Y = {cursor.ycor()}")
    y = cursor.ycor()
    if y <= -380:
        return
    y -= 40
    cursor.sety(y)
    logging.debug(f"Cursor to Y = {cursor.ycor()}")

def showItems(items):
    pen.penup()
    pen.goto()
    for item in items:
        pen.write(item, font=("Arial", 20))

# Keyboard binding
window.listen()
window.onkeypress(moveCursorUp, "Up")
window.onkeypress(moveCursorDown, "Down")


logging.info("Loop start")
generalMenu()
# showItems(items, (-230, 350))
while True:
    window.update()

    if page == "General Menu":
        generalMenu()
        page = "Pause"

    

    








