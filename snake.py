import turtle

GRID_SIZE = 20
GRID_COUNT = 20
START = -(GRID_SIZE * GRID_COUNT) / 2

class Snake:
    def __init__(self, head_color, body_color, x, y):
        self.segments = []
        self.direction = "right"
        self.next_direction = "right"

        head = turtle.Turtle()
        head.shape("square")
        head.color(head_color)
        head.shapesize(GRID_SIZE / 20)
        head.penup()
        head.goto(x * GRID_SIZE + START + GRID_SIZE / 2, y * GRID_SIZE + START + GRID_SIZE / 2)

        self.segments.append(head)

    def move(self):
        self.direction = self.next_direction

        for i in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[i-1].xcor()
            new_y = self.segments[i-1].ycor()
            self.segments[i].goto(new_x, new_y)

        head = self.segments[0]
        x = head.xcor()
        y = head.ycor()

        if self.direction == "right":
            head.goto(x + GRID_SIZE, y)
        elif self.direction == "left":
                head.goto(x - GRID_SIZE, y)
        elif self.direction == "up":
                head.goto(x, y + GRID_SIZE)
        elif self.direction == "down":
                head.goto(x, y - GRID_SIZE)

    def grow(self):
        segment = turtle.Turtle()
        segment.shape("square")
        segment.color("#B130B1")
        segment.shapesize(GRID_SIZE / 20)
        segment.penup()

        last_segment = self.segments[-1]
        segment.goto(last_segment.xcor(), last_segment.ycor())

        self.segments.append(segment)


