import turtle
import random

turtle.colormode(255)

class Snake:
    def __init__(self, head_color, body_color, x, y, get_dimensions):
        # pick snake body and head colors
        def random_color():
            r = random.randint(50, 200)
            g = random.randint(50, 200)
            b = random.randint(50, 200)
            return (r, g, b)
        
        def lighter_color(color):
             r, g, b = color
             return (min(r + 40, 255), min(g + 40, 255), min(b + 40, 255))

        self.get_dimensions = get_dimensions
        self.segments = []
        self.direction = "right"
        self.next_direction = "right"
        self.head_color = random_color()
        self.body_color = lighter_color(self.head_color)

        start, _, grid_size, _ = get_dimensions()

        head = turtle.Turtle()
        head.shape("square")
        head.color(self.head_color)
        head.shapesize(grid_size / 20)
        head.penup()
        head.goto(x * grid_size + start + grid_size / 2, y * grid_size + start + grid_size / 2)
        head.hideturtle()

        self.segments.append(head)

    # Move snake one box, shift body segments and head forward
    def move(self):
        self.direction = self.next_direction

        for i in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[i-1].xcor()
            new_y = self.segments[i-1].ycor()
            self.segments[i].goto(new_x, new_y)

        start, _, grid_size, _ = self.get_dimensions()
        head = self.segments[0]
        x = head.xcor()
        y = head.ycor()

        # Move the head one grid cell in the current direction.
        if self.direction == "right":
            head.goto(x + grid_size, y)
        elif self.direction == "left":
                head.goto(x - grid_size, y)
        elif self.direction == "up":
                head.goto(x, y + grid_size)
        elif self.direction == "down":
                head.goto(x, y - grid_size)

    # Append a new body segment at the tail of the snake.
    def grow(self):
        _, _, grid_size, _ = self.get_dimensions()

        segment = turtle.Turtle()
        segment.shape("square")
        segment.color(self.body_color)
        segment.shapesize(grid_size / 20)
        segment.penup()
        segment.hideturtle()

        last_segment = self.segments[-1]
        segment.goto(last_segment.xcor(), last_segment.ycor())

        segment.showturtle()
        self.segments.append(segment)