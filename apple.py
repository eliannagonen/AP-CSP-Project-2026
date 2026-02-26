import turtle

class Apple:
    def __init__(self, color, x, y):
        self.color = color
        self.x = x
        self.y = y
    
    def draw(self):
        t = turtle.Turtle()
        t.shape("circle")
        t.shapesize(0.5, 0.5)
        t.color(self.color)
        t.penup()
        t.hideturtle()
        t.goto(self.x * 20 - 190, self.y * 20 - 190)
        t.stamp()