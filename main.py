import turtle
import random
from snake import Snake
from apple import Apple

GRID_SIZE = 20
GRID_COUNT = 20
START = -(GRID_SIZE * GRID_COUNT) / 2
END = START + (GRID_SIZE * GRID_COUNT) - GRID_SIZE / 2

writer = turtle.Turtle()
writer.hideturtle()
writer.penup()
writer.color("#000000")

def displayInstructions():
   writer.goto(0, 0)
   writer.write(
        "~~~~~~~~~~~~~~~\n\n" \
        "         SNAKE     \n\n" \
        "~~~~~~~~~~~~~~~\n\n" \
        "Instructions:\n" \
        "> Use the arrow keys on your keyboard to control the snake.\n" \
        "> Do not let your snake reach the edges of the screen.\n" \
        "> Direct your snake to reach the red apple.\n" \
        "> Do not let your snake eat/cross its own tail.\n\n" \
        "Click the screen to get started!",
        align="center",
        font=("Arial", 12, "bold")
    )

def start_game(x, y):
    screen.onclick(None)
    writer.clear()
    update_score()
    game_loop()

def drawBorders():
   pen = turtle.Turtle()
   pen.hideturtle()  
   pen.speed(5)
   pen.color("#FFFFFF")
   pen.pensize(2)
   pen.penup()
   pen.goto(START, START)
   pen.pendown()
   for i in range(4):
      pen.forward(GRID_SIZE * GRID_COUNT)
      pen.left(90)

# Setup the Stage
screen = turtle.Screen()
screen.tracer(0,0)
screen.setup(410, 445)
screen.colormode(255)
screen.bgcolor((200,200,200))


def drawGrid():
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.speed(0)
    pen.color("#AAAAAA")
    pen.penup()

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

# Draw the white borders and grid lines
drawBorders()
drawGrid()

# Add the apple
apple = Apple("#FF0000",random.randint(0,GRID_COUNT - 1),random.randint(0,GRID_COUNT - 1))
apple.draw()

# Add the Snake
snake = Snake("","",10,10) 
snake.direction = "right"

# Display instructions on how to play the game
displayInstructions()
screen.onclick(start_game)

screen.listen()

def go_up():
    if snake.direction != "down":
        snake.next_direction = "up"

def go_down():
    if snake.direction != "up":
        snake.next_direction = "down"

def go_right():
    if snake.direction != "left":
        snake.next_direction = "right"

def go_left():
    if snake.direction != "right":
        snake.next_direction = "left"

screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")
screen.onkey(go_right, "Right")
screen.onkey(go_left, "Left")

game_running = True

def game_loop():
    global score
    snake.move()

    head = snake.segments[0]
    START = - (GRID_SIZE * GRID_COUNT) / 2

    if head.distance(apple.x * GRID_SIZE + START + GRID_SIZE / 2, apple.y * GRID_SIZE + START + GRID_SIZE / 2) < 10:
        print("Apple eaten!")
        score += 1
        apple.x = random.randint(0,GRID_COUNT - 1)
        apple.y = random.randint(0,GRID_COUNT - 1)
        apple.draw()
        snake.grow()
        update_score()

    if len(snake.segments) == GRID_COUNT * GRID_COUNT:
        writer.clear()
        writer.goto(0, 0)
        writer.write("You Win!\n\nClick to restart!", align="center", font=("Arial", 50, "bold"))
        screen.onclick(restart_game)
        return

    x = head.xcor()
    y = head.ycor()

    if x < START + GRID_SIZE / 2 or x > END or y < START + GRID_SIZE / 2 or y > END:
        print("Game Over!")
        writer.clear()
        writer.goto(0, 0)
        writer.write("Game Over!\n\nClick to restart!", align="center", font=("Arial", 20, "bold")) 
        screen.onclick(restart_game)
        return

    for segment in snake.segments[1:-1]:
        if head.distance(segment) < 5:
            print("Game Over!")
            writer.clear()
            writer.goto(0, 0)
            writer.write("Game Over!\n\nClick to restart!", align="center", font=("Arial", 20, "bold"))
            screen.onclick(restart_game)
            return
        
    screen.update()
    screen.ontimer(game_loop, 200)

score = 0

def update_score():
    writer.clear()
    writer.goto(0, 203)
    writer.write(f"Score: {score}", align="center", font=("Arial", 14, "bold"))

def restart_game(x,y):
    global score, snake
    screen.onclick(None)

    for segment in snake.segments:
        segment.hideturtle()

    score = 0
    snake = Snake("","",10,10)
    snake.direction = "right"
    apple.x = random.randint(0, GRID_COUNT - 1)
    apple.y = random.randint(0, GRID_COUNT - 1)
    apple.draw()
    writer.clear()
    update_score()
    game_loop()
turtle.done()