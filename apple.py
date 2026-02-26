import turtle

GRID_SIZE = 16

class Apple:
    def __init__(self, color, x, y):
        self.color = color
        self.x = x
        self.y = y

        self.t = turtle.Turtle()
        self.t.shape("circle")
        self.t.shapesize(0.4, 0.4)
        self.t.color(self.color)
        self.t.penup()
        self.t.hideturtle()

        self.draw()
    
    def draw(self):
        self.t.clear()
        self.t.goto(self.x * GRID_SIZE - 190, self.y * GRID_SIZE - 190)
        self.t.stamp()