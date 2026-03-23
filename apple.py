import turtle

GRID_SIZE = 20
GRID_COUNT = 20
START = -(GRID_SIZE * GRID_COUNT) / 2

class Apple:
    def __init__(self, color, x, y):
        self.color = color
        self.x = x
        self.y = y

        self.t = turtle.Turtle()
        self.t.shape("circle")
        self.t.shapesize(GRID_SIZE / 20 * 0.9, GRID_SIZE / 20 * 0.9)
        self.t.color(self.color)
        self.t.penup()
        # self.t.hideturtle()
        self.draw()
    
    def draw(self):
        # self.t.clear()
        self.t.goto(self.x * GRID_SIZE + START + GRID_SIZE / 2, self.y * GRID_SIZE + START + GRID_SIZE / 2)
        # self.t.stamp()