import turtle
import random
import time

from snake import Snake
from apple import Apple

GRID_SIZE = 16
GRID_COUNT = 20

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


def drawGrid():
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.speed(0)
    pen.color("#AAAAAA")
    pen.penup()

    GRID_SIZE = 16
    GRID_COUNT = 20
    GRID_PIXEL = GRID_SIZE * GRID_COUNT
    START = -GRID_PIXEL / 2

    # vertical lines
    for i in range(GRID_COUNT + 1):
        x = START + i * GRID_SIZE
        pen.goto(x, START)
        pen.pendown()
        pen.goto(x, START + GRID_COUNT * GRID_SIZE)
        pen.penup()

    # horizontal lines
    for i in range(GRID_COUNT + 1):
        y = START + i * GRID_SIZE
        pen.goto(START, y)
        pen.pendown()
        pen.goto(START + GRID_COUNT * GRID_SIZE, y)
        pen.penup()

# >>> Draw the white borders and grid lines
drawBorders()
drawGrid()

# >>> Add the apple
apple = Apple("#FF0000",random.randint(0,19),random.randint(0,19))
apple.draw()

# >>> Add the Snake...
snake = Snake("#810081","#B130B1",10,10)  #Purple Snake in the bottom left corner (0,0) of the 20x20 grid
snake.direction = "right"

# >>> Display instructions on how to play the game
displayInstructions()

screen.listen()

def go_up():
    if snake.direction != "down":
        snake.direction = "up"

def go_down():
    if snake.direction != "up":
        snake.direction = "down"

def go_right():
    if snake.direction != "left":
        snake.direction = "right"

def go_left():
    if snake.direction != "right":
        snake.direction = "left"

screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")
screen.onkey(go_right, "Right")
screen.onkey(go_left, "Left")

game_running = True

def game_loop():
    snake.move()

    head = snake.segments[0]

    if head.distance(apple.x * 20 - 190, apple.y * 20 - 190) < 10:
        print("Apple eaten!")
        apple.x = random.randint(0,GRID_COUNT)
        apple.y = random.randint(0,GRID_COUNT)

        apple.draw()
        snake.grow()

    screen.update()
    screen.ontimer(game_loop, 200)

    x = head.xcor()
    y = head.ycor()

    if x > 190 or x < -190 or y > 190 or y < -190:
        print("Game Over!")
        return
    
    for segment in snake.segments[1:]:
        if head.distance(segment) < 5:
            print("Game Over!")
            return

game_loop()

turtle.done()