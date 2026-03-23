import turtle

class Apple:
    def __init__(self, color, x, y, get_dimensions):
        self.color = color
        self.x = x
        self.y = y
        self.get_dimensions = get_dimensions  # callable from main

        self.t = turtle.Turtle()
        self.t.shape("circle")
        self.t.color(self.color)
        self.t.penup()
        self.t.hideturtle()

    def draw(self):
        start, _, grid_size, _ = self.get_dimensions()
        self.t.shapesize(grid_size / 20 * 0.9, grid_size / 20 * 0.9)
        self.t.goto(
            self.x * grid_size + start + grid_size / 2,
            self.y * grid_size + start + grid_size / 2
        )
        self.t.showturtle()
    
    