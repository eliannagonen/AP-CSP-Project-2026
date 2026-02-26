import turtle

class Snake:
    def __init__(self, head_color, body_color, x, y):
        self.segments = []
        self.direction = "right"

        head = turtle.Turtle()
        head.shape("square")
        head.color(head_color)
        head.shapesize(0.5)
        head.penup()
        head.goto(x * 20 - 190, y * 20 - 190)

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
            head.goto(x + 20, y)
        elif self.direction == "left":
                head.goto(x - 20, y)
        elif self.direction == "up":
                head.goto(x, y + 20)
        elif self.direction == "down":
                head.goto(x, y - 20)

