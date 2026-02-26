import turtle
import random
import time
from snake import Snake
from apple import Apple

def displayInstructions():
   print("")
   print("~~~~~~~~~~~~~~~~~~~~")
   print("                    ")
   print("    Snake Game      ")
   print("                    ")
   print("~~~~~~~~~~~~~~~~~~~~")
   print("")

   print("Instructions")
   print(" > Use the arrow keys on your keyboard to control the snake.")
   print(" > Do not let your snake reach the edges of the screen.")
   print(" > Direct your snake to reach the red apple.")
   print(" > Do not let your snake eat/cross its own tail.")
   print("")

   print(" >>> Double click on the screen to get started...")
   print("")


def drawBorders():
   pen = turtle.Turtle()
   pen.hideturtle()  
   pen.speed(5)
   pen.color("#FFFFFF")
   pen.pensize(2)
   pen.penup()
   pen.goto(-199,-199)
   pen.pendown()
   for i in range(4):
      pen.forward(398)
      pen.left(90)

# >>> Setup the Stage
screen = turtle.Screen()
screen.tracer(0,0)
screen.setup(400, 400)
screen.colormode(255)
screen.bgcolor((200,200,200))

# >>> Draw the white borders
drawBorders()


# >>> Add the apple
apple = Apple("#FF0000",random.randint(0,19),random.randint(0,19))
apple.draw()

# >>> Add the Snake...
snake = Snake("#810081","#B130B1",0,19)  #Purple Snake in the bottom left corner (0,0) of the 20x20 grid
snake.direction = "right"
snake.draw()


# >>> Display instructions on how to play the game
displayInstructions()

screen.listen()

def go_up():
   if snake.direction != "Down":
      snake.direction = "Up"

def go_down():
   if snake.direction != "Up":
      snake.direction = "Down"
def go_right():
   if snake.direction != "Left":
      snake.direction = "Right"

def go_left():
   if snake.direction != "Right":
      snake.direction = "Left"

screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")
screen.onkey(go_right, "Right")
screen.onkey(go_left, "Left")

turtle.done()