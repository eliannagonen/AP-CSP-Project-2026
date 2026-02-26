import turtle

GRID_SIZE = 16

class Snake:
    def __init__(self, head_color, body_color, x, y):
        self.segments = []
        self.direction = "right"

        head = turtle.Turtle()
        head.shape("square")
        head.color(head_color)
        head.shapesize(0.4)
        head.penup()
        head.goto(x * GRID_SIZE - 190, y * GRID_SIZE - 190)

        self.segments.append(head)

    def move(self):
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
        segment.shapesize(0.4)
        segment.penup()

        last_segment = self.segments[-1]
        segment.goto(last_segment.xcor(), last_segment.ycor())

        self.segments.append(segment)


