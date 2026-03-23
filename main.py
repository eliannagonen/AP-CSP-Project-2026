import turtle
import random
from snake import Snake
from apple import Apple

# --- Grid Constants ---
GRID_COUNT = 20  # number of cells

# --- Screen Setup ---
screen = turtle.Screen()
screen.tracer(0, 0)
screen.setup(width=0.8, height=0.8)
screen.colormode(255)
screen.bgcolor((200, 200, 200))

# Derived dynamically from window size — call get_dimensions() to get current values
def get_dimensions():
    w = screen.window_width()
    h = screen.window_height()
    margin = 40
    usable = min(w, h) - margin * 2
    grid_size = usable // GRID_COUNT
    total = grid_size * GRID_COUNT
    start = -total // 2
    end = start + total - grid_size // 2
    return start, end, grid_size, total

# --- Drawing ---
grid_turtles = []  # track grid/border turtles so we can clear just them

def drawBorders(start, total):
    pen = turtle.Turtle()
    grid_turtles.append(pen)
    pen.hideturtle()
    pen.speed(0)
    pen.color("#FFFFFF")
    pen.pensize(2)
    pen.penup()
    pen.goto(start, start)
    pen.pendown()
    for _ in range(4):
        pen.forward(total)
        pen.left(90)

def drawGrid(start, grid_size, total):
    pen = turtle.Turtle()
    grid_turtles.append(pen)
    pen.hideturtle()
    pen.speed(0)
    pen.color("#AAAAAA")
    pen.penup()

    for i in range(GRID_COUNT + 1):
        x = start + i * grid_size
        pen.goto(x, start)
        pen.pendown()
        pen.goto(x, start + total)
        pen.penup()

    for i in range(GRID_COUNT + 1):
        y = start + i * grid_size
        pen.goto(start, y)
        pen.pendown()
        pen.goto(start + total, y)
        pen.penup()

def redrawGrid():
    """Clear only grid turtles and redraw — safe to call during gameplay."""
    for pen in grid_turtles:
        pen.clear()
        pen.hideturtle()
    grid_turtles.clear()

    start, end, grid_size, total = get_dimensions()
    drawBorders(start, total)
    drawGrid(start, grid_size, total)

redrawGrid()
screen.update()

# --- Writer turtle ---
writer = turtle.Turtle()
writer.hideturtle()
writer.penup()
writer.color("#000000")

# --- Score ---
score = 0
high_score = 0

def update_score():
    _, _, _, total = get_dimensions()
    writer.clear()
    writer.goto(0, total // 2 + 10)  # just above the grid
    writer.write(f"Score: {score}   High Score: {high_score}", align="center", font=("Arial", 14, "bold"))

# --- Game objects ---
apple = Apple("#FF0000", random.randint(0, GRID_COUNT - 1), random.randint(0, GRID_COUNT - 1), get_dimensions)

snake = Snake("", "", 10, 10, get_dimensions)
snake.direction = "right"
snake.segments[0].hideturtle()

# --- Resize polling ---
game_started = False
_last_size = (0, 0)

def checkResize():
    global _last_size
    if not game_started:
        current = (screen.window_width(), screen.window_height())
        if current != _last_size:
            _last_size = current
            redrawGrid()
            screen.update()
    screen.ontimer(checkResize, 500)

checkResize()

# --- Instructions ---
def displayInstructions():
    writer.goto(0, 0)
    writer.write(
        "~~~~~~~~~~~~~~~\n\n"
        "         SNAKE     \n\n"
        "~~~~~~~~~~~~~~~\n\n"
        "Instructions:\n"
        "> Use the arrow keys to control the snake.\n"
        "> Do not hit the edges of the screen.\n"
        "> Direct your snake to the red apple.\n"
        "> Do not cross your own tail.\n\n"
        "Click the screen to get started!",
        align="center",
        font=("Arial", 12, "bold")
    )

def start_game(x, y):
    print("start_game called")
    global game_started
    game_started = True

    screen.onclick(None)
    writer.clear()

    start, _, grid_size, _ = get_dimensions()
    print(f"grid_size: {grid_size}, start: {start}")

    for segment in snake.segments:
        segment.shapesize(grid_size / 20)
        # Reposition head to its grid cell using new dimensions
    snake.segments[0].showturtle()
    snake.segments[0].goto(10 * grid_size + start + grid_size / 2, 10 * grid_size + start + grid_size / 2)
    print(f"snake head at: {snake.segments[0].xcor()}, {snake.segments[0].ycor()}")
    print(f"snake visible: {snake.segments[0].isvisible()}")

    apple.draw()
    print(f"apple at: {apple.t.xcor()}, {apple.t.ycor()}")
    print(f"apple visible: {apple.t.isvisible()}")

    update_score()
    screen.update()
    game_loop()

displayInstructions()
screen.onclick(start_game)

# --- Controls ---
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
screen.listen()

# --- Game loop ---
def place_apple():
    """Find a random grid cell not occupied by the snake."""
    while True:
        new_x = random.randint(0, GRID_COUNT - 1)
        new_y = random.randint(0, GRID_COUNT - 1)
        if not any(s.xcor() == new_x and s.ycor() == new_y for s in snake.segments):
            return new_x, new_y

def game_loop():
    global score, high_score
    snake.move()

    start, end, grid_size, _ = get_dimensions()
    head = snake.segments[0]

    # Apple eaten
    apple_px_x = apple.x * grid_size + start + grid_size / 2
    apple_px_y = apple.y * grid_size + start + grid_size / 2
    if head.distance(apple_px_x, apple_px_y) < 10:
        score += 1
        apple.x, apple.y = place_apple()
        apple.draw()
        snake.grow()
        update_score()

    # Win
    if len(snake.segments) == GRID_COUNT * GRID_COUNT:
        high_score = max(score, high_score)
        writer.clear()
        writer.goto(0, 0)
        writer.write("You Win!\n\nClick to restart!", align="center", font=("Arial", 50, "bold"))
        screen.onclick(restart_game)
        return

    x, y = head.xcor(), head.ycor()

    # Hit wall
    if x < start + grid_size / 2 or x > end or y < start + grid_size / 2 or y > end:
        high_score = max(score, high_score)
        writer.clear()
        writer.goto(0, 0)
        writer.write(f"Game Over!\n\nHigh Score: {high_score}\n\nClick to restart!", align="center", font=("Arial", 20, "bold"))
        screen.onclick(restart_game)
        return

    # Self collision
    for segment in snake.segments[1:-1]:
        if head.distance(segment) < 5:
            high_score = max(score, high_score)
            writer.clear()
            writer.goto(0, 0)
            writer.write(f"Game Over!\n\nHigh Score: {high_score}\n\nClick to restart!", align="center", font=("Arial", 20, "bold"))
            screen.onclick(restart_game)
            return

    screen.update()
    screen.ontimer(game_loop, 200)

# --- Restart ---
def restart_game(x, y):
    global score, snake
    screen.onclick(None)

    for segment in snake.segments:
        segment.hideturtle()

    score = 0

    snake = Snake("", "", 10, 10, get_dimensions)
    snake.direction = "right"
    snake.segments[0].showturtle()

    apple.x = random.randint(0, GRID_COUNT - 1)
    apple.y = random.randint(0, GRID_COUNT - 1)
    apple.draw()

    writer.clear()
    update_score()
    game_loop()

turtle.done()